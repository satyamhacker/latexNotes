## 🏰 **PHASE 0: FOUNDATIONAL INFRASTRUCTURE & SECURITY**

### 🔑 **Level 0: Authentication & Provider Security**
- **Never hardcode credentials** – use environment variables (`AWS_ACCESS_KEY_ID`), IAM instance profiles, or tools like `aws-vault`.
- **Provider aliases for multi-account/region** – manage multiple regions or accounts with aliased providers.
  ```hcl
  provider "aws" {
    alias  = "virginia"
    region = "us-east-1"
  }
  provider "aws" {
    alias  = "oregon"
    region = "us-west-2"
  }
  
  resource "aws_instance" "web_virginia" {
    provider = aws.virginia
    ami      = "ami-123"
    # ...
  }
  ```
- **Assume roles for cross-account access** – use `assume_role` in provider block.
  ```hcl
  provider "aws" {
    assume_role {
      role_arn = "arn:aws:iam::ACCOUNT_ID:role/TerraformRole"
    }
  }
  ```
- **Secure credential handling** – integrate with HashiCorp Vault or AWS Secrets Manager for dynamic, short-lived credentials.

### 📁 **Level 1: Code Organization & Repository Hygiene**
- **Standard directory structure for enterprises**:
  ```
  terraform/
  ├── modules/
  │   ├── networking/
  │   ├── compute/
  │   └── database/
  ├── environments/
  │   ├── dev/
  │   │   ├── main.tf
  │   │   ├── variables.tf
  │   │   └── terraform.tfvars (ignored by git)
  │   ├── staging/
  │   └── prod/
  └── global/ (shared resources like S3 backend, IAM roles)
  ```
- **`.gitignore` essentials** – exclude `.terraform/`, `*.tfstate`, `*.tfstate.backup`, `*.tfvars` (except example files).
- **Pre-commit hooks** – run `terraform fmt`, `terraform validate`, and security scanners automatically.
  ```bash
  # .pre-commit-config.yaml
  repos:
  - repo: https://github.com/antonbabenko/pre-commit-terraform
    rev: v1.77.0
    hooks:
      - id: terraform_fmt
      - id: terraform_validate
      - id: terraform_tfsec
      - id: terraform_checkov
  ```

### 🛡️ **Level 2: Variable Validation & Type Constraints**
- **Add validation blocks** – prevent bad inputs before `apply`.
  ```hcl
  variable "instance_type" {
    description = "EC2 instance type"
    type        = string
    
    validation {
      condition     = contains(["t2.micro", "t3.small", "t3.medium"], var.instance_type)
      error_message = "Instance type must be one of: t2.micro, t3.small, t3.medium."
    }
  }
  
  variable "environment" {
    type = string
    
    validation {
      condition     = var.environment == "dev" || var.environment == "staging" || var.environment == "prod"
      error_message = "Environment must be dev, staging, or prod."
    }
  }
  ```
- **Complex type constraints** – enforce structure for maps and objects.
  ```hcl
  variable "tags" {
    type = map(string)
    default = {
      Environment = "dev"
      ManagedBy   = "Terraform"
    }
  }
  
  variable "database_config" {
    type = object({
      engine         = string
      engine_version = string
      instance_class = string
      storage_gb     = number
    })
  }
  ```

---

## 🗃️ **PHASE 1: ADVANCED STATE MANAGEMENT & DISASTER RECOVERY**

### 💾 **Level 0: State File Security & Encryption**
- **Secrets in state** – understand that ANY resource attribute (even if marked sensitive) is stored in plain text in the state.
  ```bash
  # View what's actually in state
  terraform state pull | grep -i password
  ```
- **Mitigation strategies**:
  1. Use external secrets stores (AWS Secrets Manager, HashiCorp Vault) and reference them
  2. Enable S3 bucket encryption with KMS
  3. Restrict state file access with strict IAM policies
  4. Regularly scan state for secrets with tools like `truffleHog`
- **Sensitive outputs** – mark outputs as `sensitive = true` to prevent display in CLI.
  ```hcl
  output "database_password" {
    value     = aws_db_instance.main.password
    sensitive = true
  }
  ```

### 🔄 **Level 1: State File Backup & Disaster Recovery**
- **Enable S3 versioning** – protects against accidental deletion or corruption.
  ```hcl
  resource "aws_s3_bucket" "terraform_state" {
    bucket = "my-company-terraform-state"
    
    versioning {
      enabled = true
    }
    
    server_side_encryption_configuration {
      rule {
        apply_server_side_encryption_by_default {
          sse_algorithm = "AES256"
        }
      }
    }
  }
  ```
- **Cross-region replication** – for critical infrastructure, replicate state bucket to another region.
- **Regular exports** – automate backups of state to a secure location.
  ```bash
  # Cron job or pipeline step
  aws s3 cp s3://my-state-bucket/prod/terraform.tfstate backups/$(date +%Y%m%d)-prod.tfstate
  ```
- **Recovery drill scenario** – practice restoring from backup.
  ```bash
  # If state is corrupted
  aws s3 cp s3://my-state-bucket-backup/prod/terraform.tfstate s3://my-state-bucket/prod/terraform.tfstate
  terraform plan  # Verify recovery worked
  ```

### 🧠 **Level 2: Remote State Data Sources**
- **Share outputs between configurations** – one stack reads another stack's state.
  ```hcl
  # In networking stack (outputs.tf)
  output "vpc_id" {
    value = aws_vpc.main.id
  }
  
  output "public_subnet_ids" {
    value = aws_subnet.public[*].id
  }
  
  # In application stack
  data "terraform_remote_state" "network" {
    backend = "s3"
    
    config = {
      bucket = "my-company-terraform-state"
      key    = "prod/network/terraform.tfstate"
      region = "us-east-1"
    }
  }
  
  resource "aws_instance" "app" {
    ami           = "ami-123"
    instance_type = "t3.micro"
    subnet_id     = data.terraform_remote_state.network.outputs.public_subnet_ids[0]
    
    tags = {
      Name = "App Server"
    }
  }
  ```
- **Dependency management** – ensure stacks are applied in correct order (network → app).

### 🧪 **Level 3: State Migration & Refactoring**
- **Moving resources between state files** – `terraform state mv` for refactoring.
  ```bash
  # Before refactoring: resource defined in main.tf
  # After: moved to a module
  terraform state mv aws_instance.web module.web.aws_instance.web
  ```
- **Importing existing resources** – bring manually created resources under Terraform management.
  ```bash
  # Find resource ID in AWS console
  terraform import aws_instance.production i-1234567890abcdef0
  ```
- **Removing resources from state** – `terraform state rm` to detach without destroying.
  ```bash
  # If you want to manage a resource manually again
  terraform state rm aws_s3_bucket.legacy
  ```

---

## 🧩 **PHASE 2: PRODUCTION-GRADE MODULE DESIGN**

### 📦 **Level 0: Module Versioning & Registry**
- **Version your modules** – use Git tags or a module registry.
  ```bash
  # Tag a module release
  git tag -a "v1.2.0" -m "Add support for encryption"
  git push origin v1.2.0
  ```
- **Source module by version** – pin to specific versions.
  ```hcl
  # From Git
  module "vpc" {
    source = "git::https://github.com/company/terraform-aws-vpc.git?ref=v1.2.0"
  }
  
  # From Terraform Registry
  module "vpc" {
    source  = "terraform-aws-modules/vpc/aws"
    version = "3.14.0"
  }
  ```
- **Semantic versioning** – follow MAJOR.MINOR.PATCH:
  - MAJOR: incompatible API changes
  - MINOR: backward-compatible functionality
  - PATCH: backward-compatible bug fixes
- **Private module registry** – for internal modules, use Terraform Cloud or a simple S3-backed registry.

### 🧪 **Level 1: Testing Modules**
- **Unit tests with examples** – every module should have an `examples/` directory.
  ```
  modules/webserver/
  ├── main.tf
  ├── variables.tf
  ├── outputs.tf
  ├── README.md
  └── examples/
      ├── basic/
      │   ├── main.tf
      │   ├── terraform.tfvars.example
      │   └── outputs.tf
      └── complete/
          ├── main.tf
          └── variables.tf
  ```
- **Integration testing with Terratest** – write Go tests that actually create resources.
  ```go
  // test/webserver_test.go
  package test
  
  import (
      "testing"
      "github.com/gruntwork-io/terratest/modules/terraform"
      "github.com/stretchr/testify/assert"
  )
  
  func TestWebServerModule(t *testing.T) {
      terraformOptions := &terraform.Options{
          TerraformDir: "../examples/basic",
      }
      
      defer terraform.Destroy(t, terraformOptions)
      terraform.InitAndApply(t, terraformOptions)
      
      output := terraform.Output(t, terraformOptions, "public_ip")
      assert.NotEmpty(t, output)
  }
  ```
- **Contract testing** – ensure module outputs match expected structure.

### 🔧 **Level 2: Module Composition Patterns**
- **Compose modules** – build higher-level modules from lower-level ones.
  ```hcl
  # modules/full_environment/main.tf
  module "networking" {
    source = "../networking"
    vpc_cidr = var.vpc_cidr
  }
  
  module "compute" {
    source = "../compute"
    subnet_ids = module.networking.public_subnet_ids
    instance_type = var.instance_type
  }
  
  module "database" {
    source = "../database"
    subnet_ids = module.networking.private_subnet_ids
    database_name = var.database_name
  }
  ```
- **Avoid deep nesting** – more than 3 levels of modules makes debugging difficult.
- **Use `count` and `for_each` in modules** – create multiple instances of a module.
  ```hcl
  module "web_servers" {
    source = "../webserver"
    count  = 3
    
    name          = "web-${count.index}"
    instance_type = "t3.micro"
  }
  ```

---

## 🔄 **PHASE 3: CI/CD & AUTOMATION SAFETY**

### 🤖 **Level 0: Pipeline Stages & Artifacts**
- **Standard CI/CD pipeline**:
  1. **Validate** – `terraform fmt -check`, `terraform validate`
  2. **Plan** – `terraform plan -out=tfplan`
  3. **Human approval** (especially for prod)
  4. **Apply** – `terraform apply tfplan`
- **Store plan artifact** – pass exact plan from plan stage to apply stage.
  ```yaml
  # GitLab CI Example
  stages:
    - validate
    - plan
    - apply
  
  validate:
    stage: validate
    script:
      - terraform init
      - terraform validate
      - terraform fmt -check
  
  plan:
    stage: plan
    script:
      - terraform plan -out=tfplan
    artifacts:
      paths:
        - tfplan
  
  apply:
    stage: apply
    script:
      - terraform apply tfplan
    when: manual  # Requires human approval
    only:
      - main
  ```
- **Separate service accounts** – each environment uses different IAM roles with least privilege.

### ✅ **Level 1: Approval Gates & Safe Apply**
- **Merge request workflow** – run plan on PR, post comment with results.
  ```bash
  # In CI, capture plan and post as comment
  terraform plan -no-color > plan.txt
  # Use API to post plan.txt as comment on PR
  ```
- **Branch protection** – require maintainer approval for prod changes.
- **Avoid `-auto-approve` in production** – always require human review.
- **Prevent destructive changes** – review any `-/+` (replace) in plans carefully.

### 💰 **Level 2: Cost Estimation & Policy as Code**
- **Cost estimation with Infracost** – show cost impact before applying.
  ```bash
  # In CI pipeline
  infracost breakdown --path . --format json > cost.json
  # Post cost estimate as comment on PR
  ```
- **Policy as code with OPA/Conftest** – enforce compliance rules.
  ```bash
  # Generate plan JSON
  terraform plan -out=tfplan
  terraform show -json tfplan > plan.json
  
  # Test against policies
  conftest test plan.json --policy ./policies
  ```
- **Example policy** – no public S3 buckets.
  ```rego
  # policies/s3_public.rego
  package main
  
  deny[msg] {
    resource := input.resource_changes[_]
    resource.type == "aws_s3_bucket"
    resource.change.after.acl == "public-read"
    msg = sprintf("S3 bucket %v has public ACL", [resource.address])
  }
  ```

---

## 🚨 **PHASE 4: ZERO-DOWNTIME & DISASTER RECOVERY**

### 🔄 **Level 0: Zero-Downtime Deployments**
- **Lifecycle rules for replacements** – use `create_before_destroy` for resources that must be replaced without downtime.
  ```hcl
  resource "aws_instance" "web" {
    ami           = var.ami_id
    instance_type = var.instance_type
    
    lifecycle {
      create_before_destroy = true
    }
  }
  ```
- **Prevent accidental deletion** – add `prevent_destroy = true` on critical resources.
  ```hcl
  resource "aws_db_instance" "production" {
    # ... database config
    
    lifecycle {
      prevent_destroy = true
    }
  }
  ```
- **Ignore changes** – avoid unnecessary replacements for attributes that change frequently.
  ```hcl
  resource "aws_autoscaling_group" "app" {
    # ... ASG config
    
    lifecycle {
      ignore_changes = [
        desired_capacity,  # Changed by autoscaling
        tags,              # Changed by other tools
      ]
    }
  }
  ```

### 🌍 **Level 1: Multi-Region & Disaster Recovery**
- **Active-passive multi-region design**:
  ```hcl
  # Primary region (us-east-1)
  provider "aws" {
    alias  = "primary"
    region = "us-east-1"
  }
  
  # Secondary region (us-west-2) for DR
  provider "aws" {
    alias  = "secondary"
    region = "us-west-2"
  }
  
  module "app_primary" {
    source     = "./modules/app"
    providers = {
      aws = aws.primary
    }
    environment = "prod-primary"
  }
  
  module "app_secondary" {
    source     = "./modules/app"
    providers = {
      aws = aws.secondary
    }
    environment = "prod-dr"
    # Disabled by default, enable during DR
    count = var.dr_enabled ? 1 : 0
  }
  ```
- **Data replication** – use RDS cross-region replicas, S3 CRR.
- **DNS failover** – Route53 health checks with failover routing.

### 🧯 **Level 2: Incident Response Runbooks**
- **Scenario: State file corrupted**:
  ```bash
  # 1. Identify corruption
  terraform plan  # Fails with state error
  
  # 2. Restore from versioned backup
  aws s3api get-object --bucket my-state-bucket \
    --key prod/terraform.tfstate \
    --version-id "latest-good-version" \
    restored.tfstate
  
  # 3. Push restored state
  aws s3 cp restored.tfstate s3://my-state-bucket/prod/terraform.tfstate
  
  # 4. Verify
  terraform plan
  ```
- **Scenario: Partial apply failure**:
  ```bash
  # 1. Identify what was created
  terraform state list
  
  # 2. Manually clean up partially created resources
  aws ec2 terminate-instances --instance-ids i-12345
  
  # 3. Remove from state
  terraform state rm aws_instance.partial
  
  # 4. Fix code and reapply
  ```
- **Scenario: Accidental resource deletion**:
  ```bash
  # 1. Check if resource still exists in AWS
  aws ec2 describe-instances --instance-ids i-12345
  
  # 2. If deleted, restore from snapshot/backup
  aws rds restore-db-instance-from-db-snapshot \
    --db-instance-identifier mydb \
    --db-snapshot-identifier mydb-final-snapshot
  
  # 3. Import back to Terraform
  terraform import aws_db_instance.mydb mydb
  ```

---

## 🔬 **PHASE 5: ADVANCED OPTIMIZATION & TROUBLESHOOTING**

### ⚡ **Level 0: Performance Optimization**
- **Parallelism control** – limit concurrent operations for API rate limits.
  ```bash
  terraform apply -parallelism=10  # Default is 10, reduce for large environments
  ```
- **Targeted applies** – only apply specific resources (use sparingly).
  ```bash
  # For emergency fixes only
  terraform apply -target=aws_instance.web -target=aws_security_group.web_sg
  ```
- **Refresh only mode** – update state without changing resources.
  ```bash
  terraform apply -refresh-only
  ```

### 🔍 **Level 1: Debugging & Logging**
- **Enable TF_LOG for debugging**:
  ```bash
  export TF_LOG=DEBUG
  export TF_LOG_PATH=terraform.log
  terraform apply
  ```
- **Log levels**: TRACE (most verbose), DEBUG, INFO, WARN, ERROR
- **Graph visualization** – understand dependencies.
  ```bash
  terraform graph | dot -Tpng > graph.png
  ```
- **State inspection commands**:
  ```bash
  terraform show  # Show current state
  terraform state list  # List all resources
  terraform state show aws_instance.web  # Show specific resource details
  ```

### 📊 **Level 2: Cost Optimization**
- **Resource tagging for cost allocation**:
  ```hcl
  locals {
    common_tags = {
      Environment = var.environment
      Project     = var.project_name
      ManagedBy   = "Terraform"
      CostCenter  = var.cost_center
    }
  }
  
  resource "aws_instance" "web" {
    # ...
    tags = local.common_tags
  }
  ```
- **Use spot instances for non-critical workloads**:
  ```hcl
  resource "aws_spot_instance_request" "worker" {
    ami           = var.ami_id
    instance_type = "t3.large"
    spot_price    = "0.03"  # Maximum bid price
    spot_type     = "one-time"
    
    # Associate with our main instance resource
    volume_tags = {
      Name = "spot-worker"
    }
  }
  ```
- **Schedule start/stop for dev environments** – use Lambda + Instance Scheduler.

---

## 📚 **Quick Reference: Must-Know Keywords for Self-Study**

| Category | Search Terms |
|----------|--------------|
| **Security** | `terraform secrets management`, `terraform sensitive data in state`, `terraform assume role cross account`, `terraform aws vault integration` |
| **State** | `terraform remote state data source`, `terraform state mv vs rm`, `terraform state recovery s3 versioning`, `terraform import existing resources` |
| **Modules** | `terraform module versioning semver`, `terraform private module registry`, `terratest module testing` |
| **CI/CD** | `terraform gitlab ci pipeline`, `terraform plan approval workflow`, `infracost terraform ci`, `conftest terraform policy` |
| **Operations** | `terraform create before destroy`, `terraform prevent destroy`, `terraform zero downtime deployment`, `terraform multi region dr` |
| **Troubleshooting** | `terraform graph visualization`, `terraform tf_log debugging`, `terraform targeted apply` |

---

