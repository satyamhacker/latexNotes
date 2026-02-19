## 🏰 **PHASE 0: FOUNDATIONAL INFRASTRUCTURE & OS**
*Before writing a single playbook, ensure your control and managed nodes are production‑ready.*

### ⚙️ **Level 0: Control Node Setup**
- **Install Ansible from official sources** – use distribution packages or a Python virtual environment with `requirements.txt`.
- **Python version** – ensure Python 3.6+; manage dependencies via `pip`.
- **Dedicated automation user** – create a non‑root user (e.g., `ansible`) and generate an SSH key pair (`ed25519`).
- **SSH config** – use `~/.ssh/config` to simplify connections (user, identity file, etc.).
- **Basic `ansible.cfg`** – set default inventory path, logging, and initial parameters.
- **Ansible Config Precedence** – know the hierarchy to debug configuration issues:
  1. `ANSIBLE_CONFIG` environment variable
  2. `ansible.cfg` in the current directory
  3. `~/.ansible.cfg` (user home)
  4. `/etc/ansible/ansible.cfg` (global)
- **Verify with** `ansible --version` to see which config file is active.

### 🛡️ **Level 1: Managed Node Hardening**
- **Create automation user** on every managed node with the same UID (optional) and limited sudo privileges.
- **SSH key distribution** – `ssh-copy-id` or an initial bootstrap playbook.
- **SSH hardening** – disable root login, password authentication; enable key‑based access only.
- **Host key management** – **never** disable host key checking in production. Pre‑populate `known_hosts` using `ssh-keyscan` or the `known_hosts` module.
- **Time synchronization** – NTP/chrony configured on all nodes.
- **Disk space monitoring** – use Ansible facts or custom scripts to alert on low disk space.

---

## 🔧 **PHASE 1: CORE ANSIBLE ESSENTIALS**
*These are the building blocks you already know—now formalize them with production best practices.*

### 📄 **Level 2: Inventory Management**
- **Static inventory** (INI/YAML) – group hierarchies, host variables, patterns.
- **Inventory parameters** – `ansible_host`, `ansible_user`, `ansible_port`, `ansible_ssh_private_key_file`.
- **Group nesting** – `[webservers:children]` and `[webservers:vars]`.
- **Dynamic inventory introduction** – understanding when static fails (brief intro to Phase 4).

### 🧩 **Level 3: Playbooks & Modules**
- **YAML syntax** – strict rules (spaces, not tabs).
- **Play structure** – `hosts`, `become`, `vars`, `tasks`, `handlers`.
- **Core modules** – `copy`, `template`, `file`, `user`, `package`, `service`, `command`, `shell`, `lineinfile`.
- **Idempotence** – core principle; prefer modules that are idempotent by design.

### 🔍 **Level 4: Variables, Facts, and Templating**
- **Variable precedence** – understand the full order (extra vars → play vars → host vars → group vars → role defaults).
- **Facts** – `gather_facts: yes`, `setup` module, and how to use `ansible_facts`.
- **Jinja2 templating** – `{{ }}` for expressions, filters (`default`, `regex_replace`, `map`), tests (`is defined`).
- **Advanced Data Parsing** – `json_query` (JMESPath) to extract specific data from complex JSON structures returned by API calls or commands.
  ```yaml
  - name: Get public IP from EC2 info
    set_fact:
      public_ip: "{{ ec2_info.instances | json_query('[0].public_ip_address') }}"
  ```

### 🔁 **Level 5: Control Structures**
- **Loops** – `loop` (preferred) vs older `with_*`; working with lists and hashes.
- **Conditionals** – `when` with `and`/`or`, comparisons, and using facts/registered variables.
- **Handlers** – notify and trigger, handler execution order, and `listen` for multiple events.

### 📦 **Level 6: Roles for Reusability**
- **Role directory structure** (`tasks`, `handlers`, `templates`, `files`, `vars`, `defaults`, `meta`).
- **`defaults/` vs `vars/`** – precedence and when to use each.
- **Role dependencies** – define in `meta/main.yml`.
- **Ansible Galaxy** – finding, using, and creating roles.

---

## 🔐 **PHASE 2: SECURITY & SECRETS MANAGEMENT**
*Protect your infrastructure and data with robust security practices.*

### 👤 **Level 7: Privilege Escalation**
- **Apply `become` sparingly** – only on tasks that need elevated privileges.
- **Use `become_user`** – e.g., `become_user: postgres` for database tasks.
- **Sudoers configuration** – grant the automation user passwordless sudo for specific commands only.

### 🔑 **Level 8: Ansible Vault**
- **Creating encrypted files** – `ansible-vault create secrets.yml`
- **Editing and rekeying** – `ansible-vault edit`, `ansible-vault rekey`
- **Using vault passwords** – `--ask-vault-pass` or vault‑password files (secured, never committed).
- **Encrypting single strings** – `ansible-vault encrypt_string 's3cret' --name 'db_password'`
- **Vault IDs** – multiple passwords for different environments (`--vault-id dev@dev-prompt`).

### 🚫 **Level 9: Secret Exposure Prevention**
- **`no_log: true`** – hide sensitive task output.
- **Never hardcode secrets** – use vault or external lookups.
- **Pre‑commit hooks** – prevent accidental secret commits.
- **Audit playbooks** – regularly scan for plaintext secrets.

### 🔌 **Level 10: External Secrets Integration (Lookups)**
- **Lookup plugins** – fetch secrets at runtime:
  - `lookup('amazon.aws.secretsmanager_secret', 'mysecret')`
  - `lookup('community.hashi_vault.vault', 'secret/data/mypath')`
  - `lookup('env', 'MY_ENV_VAR')`
- **Modules for secrets** – `aws_secret`, `hashi_vault` to manage secrets.
- **Short‑lived credentials** – use AWS STS, etc., to avoid long‑lived keys.

### 🔑 **Level 11: SSH Key Management**
- **SSH key distribution** – automate with `authorized_key` module.
- **Host key verification** – use `known_hosts` module to manage host keys centrally.
- **SSH bastion/jump hosts** – configure via `ProxyCommand` or `ansible_ssh_common_args`.

---

## 🧪 **PHASE 3: RELIABILITY, TESTING & ERROR HANDLING**
*Make your automation robust and trustworthy.*

### 🧱 **Level 12: Idempotency Deep Dive**
- **Idempotent modules** – always prefer them.
- **Making `command`/`shell` idempotent** – use `creates`, `removes`, `changed_when`, `failed_when`.
- **`changed_when`** – define what constitutes a change based on output.
  ```yaml
  - name: Update app
    command: /opt/app/update.sh
    register: result
    changed_when: "'updated' in result.stdout"
  ```
- **`failed_when`** – custom failure conditions.

### 🛠️ **Level 13: Error Handling with Blocks**
- **`block`, `rescue`, `always`** – structured error recovery.
- **Rollback patterns** – restore previous state on failure.
- **Example**:
  ```yaml
  - block:
      - name: Deploy new config
        template: src=app.conf.j2 dest=/etc/app/app.conf
      - name: Restart service
        service: name=app state=restarted
    rescue:
      - name: Rollback config
        copy: src=/backup/app.conf dest=/etc/app/app.conf
      - fail: msg="Deployment failed"
    always:
      - name: Clean up temp files
        file: path=/tmp/deploy.tmp state=absent
  ```

### 🔬 **Level 14: Testing & Validation**
- **Check mode** (`--check`) – dry‑run changes.
- **Diff mode** (`--diff`) – see exact file modifications.
- **Syntax check** – `ansible-playbook --syntax-check playbook.yml`
- **Linting** – `ansible-lint` (integrate into CI/CD).
- **Molecule** – test roles in isolated containers or VMs before production.
- **Debugging CLI Mastery**:
  - `--start-at-task="Task Name"` – resume execution from a specific task.
  - `--step` – interactive confirmation before each task.
  - `-vvvv` – maximum verbosity, showing raw SSH chatter.
  - Use retry files: after a failure, re‑run only failed hosts with `--limit @playbook.retry`.

### ⏱️ **Level 15: Asynchronous Tasks & Polling**
- **`async` and `poll`** – run long‑running tasks without timing out:
  ```yaml
  - name: Long running operation
    command: /opt/long_task.sh
    async: 1800
    poll: 10
  ```
- **Fire‑and‑forget** – set `poll: 0` and check status later with `async_status`.

---

## ⚡ **PHASE 4: SCALING & PERFORMANCE**
*Handle thousands of nodes efficiently and with minimal downtime.*

### 🚀 **Level 16: Performance Tuning**
- **`forks`** – increase parallelism (e.g., `forks=50` in `ansible.cfg`).
- **SSH pipelining** – `pipelining = True` (requires `requiretty` disabled).
- **`gather_facts: no`** – skip fact gathering when not needed.
- **Facts caching** – use Redis, JSON, or `ansible-cmdb` to avoid repeated fact gathering.
- **ControlPersist** – enable SSH multiplexing:
  ```ini
  ssh_args = -o ControlMaster=auto -o ControlPersist=60s
  ```
- **`strategy: free`** – let hosts run independently (use with caution).

### 🔄 **Level 17: Rolling Updates & Zero‑Downtime Deployments**
- **`serial`** – update hosts in batches (e.g., `serial: "20%"` or `serial: 1` for canary).
- **`max_fail_percentage`** – abort if failure rate exceeds threshold.
- **`throttle`** – limit concurrency for specific tasks.
- **Integration with load balancers** – remove node from LB, update, then reattach.

### ☁️ **Level 18: Dynamic Inventory**
- **Why static fails at scale** – IPs change, auto‑scaling.
- **Dynamic inventory plugins** (preferred over scripts):
  - `aws_ec2` – filter by tags, regions.
  - `gcp_compute`, `azure_rm`, `vmware_vm_inventory`, etc.
- **Example `aws_ec2.yml`**:
  ```yaml
  plugin: amazon.aws.aws_ec2
  regions:
    - us-east-1
  filters:
    tag:Environment: production
  keyed_groups:
    - key: tags.Role
  ```
- **Testing** – `ansible-inventory -i aws_ec2.yml --graph`

### 🏷️ **Level 19: Tagging for Targeted Execution**
- **Add tags to tasks, plays, or roles** – e.g., `tags: deploy, config`.
- **Run with `--tags` or `--skip-tags`** – execute only relevant parts.
- **Tag inheritance** – tags applied to a play apply to all its tasks.

### 🔁 **Level 20: Pull‑Based Configuration with Ansible-Pull**
- **Concept** – instead of pushing from a control node, managed nodes pull their configuration from a Git repository at regular intervals or at boot.
- **Use Case** – auto‑scaling groups: new instances self‑configure without waiting for a central server.
- **Command example**:
  ```bash
  ansible-pull -U https://github.com/company/ansible.git playbook.yml
  ```
- **Integration with cron or systemd timers** for periodic convergence.

---

## 🏛️ **PHASE 5: PRODUCTION‑GRADE CODE STRUCTURE & ECOSYSTEM**
*Organize your automation for maintainability, collaboration, and enterprise integration.*

### 📦 **Level 21: Collections & Fully Qualified Collection Names (FQCN)**
- **Collections** – packaging format for roles, modules, plugins.
- **FQCN** – use namespaced module names to avoid conflicts and ensure clarity:
  ```yaml
  - name: Copy file
    ansible.builtin.copy:
      src: foo
      dest: bar
  ```
- **Manage collections** – create a `requirements.yml`:
  ```yaml
  collections:
    - name: community.aws
      version: '>=5.0.0'
  ```
- **Install** – `ansible-galaxy collection install -r requirements.yml`

### 📁 **Level 22: Advanced Role Design**
- **Default variables** – lowest precedence; define safe defaults in `defaults/main.yml`.
- **Role variables** – higher precedence; use `vars/main.yml` for internal constants.
- **Role dependencies** – declare in `meta/main.yml`.
- **Ansible Galaxy** – publish and consume community roles.

### 🖥️ **Level 23: AWX / Ansible Automation Controller**
- **AWX** – open‑source web UI for Ansible; **Ansible Automation Platform** is the enterprise version.
- **Core concepts**:
  - **Projects** – sync playbooks from Git.
  - **Inventories** – static or dynamic.
  - **Credentials** – manage SSH keys, vault passwords, cloud secrets.
  - **Job Templates** – parameterized playbook runs.
  - **Workflows** – chain multiple job templates.
  - **RBAC** – fine‑grained access control.
- **Centralized logging & auditing** – all job runs are recorded.

### 📊 **Level 24: Observability & Callback Plugins**
- **Ansible logging** – enable `log_path` in `ansible.cfg`.
- **Callback plugins** – send results to external systems (Slack, Splunk, ELK, etc.).
  - `ansible.posix.json` – structured JSON output.
  - Custom callbacks – write your own.
- **Profiling** – `ansible-profiler` to identify slow tasks.

---

## 🚀 **PHASE 6: MODERN ANSIBLE – BEYOND THE CLI**
*Embrace the latest innovations to build self‑healing, containerized, and event‑driven automation.*

### 🐳 **Level 25: Execution Environments & Ansible Navigator**
- **Execution Environments (EE)** – containerized Ansible environments with pinned dependencies.
- **Ansible Builder** – create custom EEs:
  ```bash
  ansible-builder build --tag my-ee:latest
  ```
- **Ansible Navigator** – modern CLI to run playbooks inside EEs:
  ```bash
  ansible-navigator run playbook.yml --eei my-ee:latest
  ```
- **Benefits** – environment parity, easier dependency management, consistent runs across CI/CD and dev machines.

### ⚡ **Level 26: Event‑Driven Ansible (EDA)**
- **Concept** – Ansible listens for events and triggers automation automatically.
- **Components**:
  - **Event sources** – webhooks, Kafka, Prometheus alerts, etc.
  - **Rulebooks** – YAML files defining `when` an event should trigger `actions` (playbooks).
  - **EDA Controller** – platform to manage and run rulebooks.
- **Example rulebook snippet**:
  ```yaml
  - name: Restart on high CPU
    hosts: all
    sources:
      - name: listen for alerts
        ansible.eda.alertmanager:
          host: 0.0.0.0
          port: 8000
    rules:
      - condition: event.alert.name == "High CPU"
        action:
          run_playbook:
            name: restart-service.yml
  ```
- **Self‑healing infrastructure** – automatically fix common issues without human intervention.

### ☸️ **Level 27: Ansible for Kubernetes & Cloud‑Native**
- **Kubernetes modules** – `community.kubernetes` or `k8s`:
  ```yaml
  - name: Create a pod
    k8s:
      state: present
      definition:
        apiVersion: v1
        kind: Pod
        metadata:
          name: my-pod
  ```
- **Helm module** – manage Helm charts:
  ```yaml
  - name: Deploy Helm chart
    helm:
      name: my-release
      chart: stable/nginx
      namespace: default
  ```
- **Ansible Operator SDK** – build Kubernetes operators using Ansible to automate application lifecycle.

### 🔌 **Level 28: Lookup Plugins for Dynamic Data**
- **Built‑in lookups** – `file`, `pipe`, `env`, `template`, `url`, etc.
- **Cloud lookups** – `amazon.aws.aws_secret`, `community.hashi_vault.vault`.
- **Use in playbooks**:
  ```yaml
  vars:
    secret: "{{ lookup('amazon.aws.secretsmanager_secret', 'my-secret') }}"
  ```

---

## 🏗️ **PHASE 7: ARCHITECT-LEVEL LOGIC & EXECUTION**
*At this level, you control **where** and **how** tasks run, ensuring zero-drift and high efficiency.*

### 🎯 **Level 29: Task Delegation & Local Actions**
- **`delegate_to`** – run a task on a host other than the current managed node (e.g., remove server from LB before update).
- **`run_once: true`** – execute a task only once per batch (e.g., DB schema update).
- **`local_action`** – shorthand for `delegate_to: localhost`.
  ```yaml
  - name: Wait for webserver to come back online
    local_action:
      module: wait_for
      host: "{{ inventory_hostname }}"
      port: 80
      state: started
  ```

### 🚦 **Level 30: Strategy Plugins (The Speed Dial)**
- **`strategy: free`** – each host runs the playbook independently, not waiting for others.
- **`strategy: host_pinned`** – keeps a worker pinned to a specific host for cache efficiency.
- **Configure in playbook**:
  ```yaml
  - hosts: all
    strategy: free
    tasks: ...
  ```

### 🏗️ **Level 31: Lifecycle Hooks (`pre_tasks` & `post_tasks`)**
- **Order of Execution**:
  1. **`pre_tasks`** – silence monitoring, put host in maintenance mode.
  2. **`roles`** – core logic.
  3. **`tasks`** – additional unique tasks.
  4. **`post_tasks`** – re‑enable alerts, send notifications.
- **Handlers** run automatically between these stages if changes occur.

---

## 🔌 **PHASE 8: EXTENSIBILITY & MULTI-PLATFORM OPS**
*A Principal Architect manages the **whole** stack: Linux, Windows, Network, and custom code.*

### 🐍 **Level 32: Custom Modules & Filter Plugins**
- **`library/`** – place custom Python modules here.
- **`filter_plugins/`** – place custom Jinja2 filters here.
- **When to write custom modules** – when no existing module fits your legacy tool or proprietary system.

### 🌐 **Level 33: Network Automation & Resource Modules**
- **Connection plugins** – `network_cli`, `netconf`, `httpapi`.
- **Key variables** – `ansible_network_os`, `ansible_connection`.
- **Resource modules** – use `config` and `state` (merged, replaced, overridden, deleted) to enforce network state.
- **Examples** – Cisco IOS, Juniper, Arista modules.

### 🪟 **Level 34: Windows Automation (The WinRM Bridge)**
- **Connection methods** – WinRM (default) or OpenSSH for Windows.
- **Initial setup** – run `ConfigureRemotingForAnsible.ps1` on Windows hosts.
- **Key modules** – `win_package`, `win_service`, `win_feature`, `win_command`.

---

## 🏷️ **PHASE 9: ADVANCED INVENTORY TARGETING**
*Precise control over which servers are "hit" by a playbook.*

### 🎯 **Level 35: Patterns & Regex Targeting**
- **Intersection (`&`)** – target hosts in both groups: `--limit "webservers:&production"`
- **Exclusion (`!`)** – target hosts in one group but not another: `--limit "webservers:!staging"`
- **Regex targeting (`~`)** – for complex naming: `--limit "~(web|db).*\.mumbai\.aws"`

---

## ✅ **FINAL CHECKLIST – FROM BEGINNER TO EXPERT**

| Phase | Focus Area | Key Topics |
|-------|------------|------------|
| **0** | Infrastructure & OS | Control node, SSH hardening, host keys, automation user, NTP, disk monitoring, config precedence |
| **1** | Core Ansible Essentials | Inventory, playbooks, modules, variables, facts, loops, conditionals, handlers, roles, `json_query` |
| **2** | Security & Secrets | Privilege escalation, Ansible Vault, `no_log`, vault IDs, external secret lookups, SSH key management |
| **3** | Reliability & Testing | Idempotency (`creates`, `changed_when`), error handling (`block`/`rescue`), check/diff mode, linting, Molecule, async tasks, debugging flags |
| **4** | Scaling & Performance | Forks, pipelining, fact caching, rolling updates (`serial`), dynamic inventory, tags, ansible-pull |
| **5** | Production‑Grade Code | FQCN, collections, role design, AWX/Automation Controller, callback plugins, logging |
| **6** | Modern Ansible | Execution Environments, Ansible Navigator, Event‑Driven Ansible, Kubernetes integration, advanced lookups |
| **7** | Architect‑Level Logic | Delegation, `run_once`, strategy plugins, `pre_tasks`/`post_tasks` |
| **8** | Extensibility & Multi‑Platform | Custom modules/filters, network automation, Windows automation |
| **9** | Advanced Targeting | Patterns, regex, intersections, exclusions |

---

## 🔍 **MASTER SEARCH KEYWORDS**
- `ansible config precedence`
- `ansible debugging flags start-at-task`
- `ansible-pull tutorial`
- `ansible json_query examples`
- `ansible execution environments best practices`
- `ansible navigator tutorial`
- `event-driven ansible rulebook examples`
- `ansible kubernetes operator sdk`
- `ansible lookup plugins external secrets`
- `ansible async poll long running tasks`
- `ansible callback plugins custom`
- `ansible tagging strategy`
- `ansible awx job templates workflows`
- `ansible delegate_to run_once`
- `ansible strategy free vs linear`
- `ansible pre_tasks post_tasks`
- `ansible custom modules filter plugins`
- `ansible network automation resource modules`
- `ansible windows winrm setup`
- `ansible inventory patterns regex`

---

