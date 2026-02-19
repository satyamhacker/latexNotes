## 🏰 PHASE 0: FOUNDATION & CLUSTER BASICS

### **Level 1: Cluster Setup & Access**
- [ ] **Static Pods** – What they are, how they are managed directly by kubelet, use cases (control plane components).

---

## 🔧 PHASE 1: CORE WORKLOADS & CONFIGURATION

### **Level 0: Controllers – Expand Coverage**
- [ ] **Init Containers** – Purpose, YAML example, use cases (e.g., waiting for a service, initializing data).
- [ ] **Jobs & CronJobs** – Complete explanation with YAML, restart policies, parallelism, and use cases (batch processing, scheduled tasks).

### **Level 1: Configuration & Secrets – Missing Security Details**
- [ ] **etcd Encryption at Rest** – Why needed, how to enable (EncryptionConfiguration), impact on performance.
- [ ] **External Secrets Operator (ESO)** – Concept, benefits, YAML example (syncing from AWS Secrets Manager / Vault).
- [ ] **SealedSecrets** – How to encrypt secrets for Git storage, installation, and usage.
- [ ] **ImagePullSecrets** – How to create and attach to pods (already mentioned but needs explicit YAML).

### **Level 1: Resource Management – Missing Features**
- [ ] **LimitRange** – Explanation, YAML examples for default CPU/memory per container.
- [ ] **ResourceQuota** – Explanation, YAML examples for namespace‑level limits.

### **Level 2: Health Checks & Lifecycle – Missing Graceful Shutdown**
- [ ] **Graceful Shutdown** – `preStop` lifecycle hook, `terminationGracePeriodSeconds`, and how applications should handle SIGTERM (with code examples).

---

## 🌐 PHASE 2: NETWORKING & SECURITY

### **Level 1: Advanced Networking – Deep Dive**
- [ ] **CNI (Container Network Interface)** – Explanation of how pods get IPs, common plugins (Calico, Cilium, Flannel), and their differences.
- [ ] **Kube-proxy Modes** – iptables vs IPVS, performance implications, how to check and change the mode.
- [ ] **CoreDNS Troubleshooting** – Common failure scenarios (DNS resolution failures), debugging commands (`nslookup`, logs), and configuration.
- [ ] **Network Policies – Full Coverage**
  - Default deny all (ingress/egress).
  - Allow specific traffic based on labels, namespaces, IP blocks.
  - Egress rules.
  - Troubleshooting network policies.

### **Level 2: Cluster Security – New Topics**
- [ ] **Pod Security Standards (PSS) / Pod Security Admission** – Explanation of the three levels (privileged, baseline, restricted), how to enforce via namespace labels, migration from PSP.
- [ ] **Security Context** – Detailed YAML examples (`runAsNonRoot`, `runAsUser`, `readOnlyRootFilesystem`, capability drops).
- [ ] **Seccomp / AppArmor Profiles** – Introduction, how to apply profiles to containers.
- [ ] **Policy Engines** – OPA/Gatekeeper or Kyverno basics, example policy (e.g., enforce image registry).

---

## 🚀 PHASE 3: RESILIENCE & STORAGE

### **Level 0: Scaling & Autoscaling – Missing Components**
- [ ] **Vertical Pod Autoscaler (VPA)** – How it works, modes (Off, Auto, Initial), YAML example, interaction with HPA.
- [ ] **Cluster Autoscaler** – Explanation, cloud‑provider configuration (AWS, GCP, Azure), interaction with HPA.
- [ ] **Custom Metrics for HPA** – Using Prometheus adapter, example HPA with custom metric (e.g., requests per second).

### **Level 1: High Availability & Spread – Missing Topics**
- [ ] **Pod Topology Spread Constraints** – Detailed explanation, YAML examples for zone and node spreading, `maxSkew`, `whenUnsatisfiable`.
- [ ] **Pod Disruption Budgets (PDB)** – Expand with more examples (`minAvailable` vs `maxUnavailable`), use during node drains, and how to test.

### **Level 2: Storage & Data – Deep Dive**
- [ ] **StorageClasses** – Explanation, YAML examples for different cloud providers (AWS EBS, GCE PD, Azure Disk), parameters.
- [ ] **Access Modes** – Detailed explanation of RWO, ROX, RWX, and when to use each.
- [ ] **Reclaim Policies** – Retain vs Delete, examples and implications.
- [ ] **CSI Drivers** – How they work, common drivers (AWS EBS CSI, Azure Disk CSI), and example usage.

### **Level 3: Backup & Disaster Recovery – Entirely New**
- [ ] **etcd Backup & Restore** – Full commands (`etcdctl snapshot save`, restore procedure).
- [ ] **Velero** – Installation, backup schedules, restore, including PV snapshots.
- [ ] **Application‑Level Backups** – Database dumps vs volume snapshots, consistency considerations.
- [ ] **Restore Testing & RTO/RPO** – Why it’s critical, how to define and test.

---

## 🔍 PHASE 4: OBSERVABILITY & TROUBLESHOOTING

### **Level 0: Monitoring & Logging – Missing Stack**
- [ ] **Prometheus Operator** – Installation (helm), ServiceMonitor concept, example.
- [ ] **kube‑state‑metrics** – What it exposes, why needed.
- [ ] **Metrics Server** – Installation, enabling `kubectl top`.
- [ ] **Logging Stack** – EFK (Elasticsearch, Fluentd, Kibana) or Loki + Promtail: explanation, DaemonSet for log collection.

### **Level 1: Debugging Toolkit – Missing Advanced Commands**
- [ ] **`kubectl debug`** – Ephemeral containers, usage examples.
- [ ] **Formal Runbooks** – Step‑by‑step troubleshooting for:
  - ImagePullBackOff
  - CrashLoopBackOff
  - Pending pods (resource, PVC, node selector)
  - Empty service endpoints
  - DNS resolution failures
- [ ] **Distributed Tracing** – Jaeger or Tempo introduction, use in microservices.

---

## 🧩 PHASE 5: ADVANCED PRODUCTION PATTERNS

### **Level 1: GitOps – New**
- [ ] **ArgoCD / Flux** – Core concepts, Application CRD, sync policies (automated, self‑heal), rollback via Git revert.
- [ ] **Multi‑Environment Management** – Using Kustomize or Helm overlays with ArgoCD.

### **Level 2: Operators & Custom Resources – New**
- [ ] **CustomResourceDefinition (CRD)** – Explanation, example CRD.
- [ ] **Operator Pattern** – What operators do, popular examples (Prometheus Operator, MySQL Operator, Cert‑Manager).

### **Level 3: Service Mesh – New**
- [ ] **Istio / Linkerd** – Value proposition (mTLS, traffic splitting, observability), basic architecture, canary deployment example.

---

## 💰 COST OPTIMIZATION (Often Overlooked but Critical)

- [ ] **Kubecost / OpenCost** – Installation, identifying cost by namespace/label.
- [ ] **Rightsizing with VPA** – Using VPA recommendations to reduce over‑provisioning.
- [ ] **Spot / Preemptible Instances** – Taints, tolerations, and node affinity for fault‑tolerant workloads.

---

## 🧪 COMMANDS & CODE SNIPPETS TO ADD

For each missing topic above, include relevant commands and YAML snippets. Here are some specific commands you may not have:

- `etcdctl snapshot save /backup.db` (with endpoints and certs)
- `velero install`, `velero schedule create`, `velero restore create`
- `kubectl debug pod/<pod> -it --image=busybox --target=<container>`
- `kubectl taint nodes <node> key=value:NoSchedule`
- `kubectl label namespace <ns> pod-security.kubernetes.io/enforce=restricted`
- `kubectl create secret docker-registry regcred ...`
- `helm install prometheus prometheus-community/kube-prometheus-stack`
- `kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml`
- `kubectl run test --rm -it --image=busybox -- nslookup <service>`

Also, for each missing YAML concept, provide a ready‑to‑use example (e.g., NetworkPolicy with egress, Pod with security context, VPA object).

---
