## 🎯 Topic 13 - Systemd Unit Files (Custom Services)

### 🐣 1. Simple Analogy

Socho tumhare paas ek **robot (application)** hai jo tumhara kaam karta hai. Tum chahte ho ki:

- Robot **server reboot ke baad apne aap start ho jaye** (enable)
- Agar robot kaam karte-karte band ho jaye, toh **apne aap restart ho** (auto-restart)
- Robot **kis user ke roop mein chale** (security)

**Systemd unit file** = Robot ka **programming card** — ismein likha hota hai ki robot ko kaise chalana hai, kab chalana hai, aur kis authority ke saath.

---

### 📖 2. Technical Definition & What

**Systemd** = Init system (PID 1) jo Linux boot ke time sabse pehle start hota hai aur saare services manage karta hai.

**Unit file** = `.service` file (usually in `/etc/systemd/system/`) jo systemd ko batati hai ki ek service ko kaise control karna hai.

**Basic Structure:**

```ini
[Unit]
Description=My Custom App
After=network.target   # Iske baad start karo

[Service]
Type=simple
User=appuser
Group=appgroup
WorkingDirectory=/opt/myapp
ExecStart=/usr/bin/python3 /opt/myapp/app.py
Restart=on-failure
RestartSec=10
EnvironmentFile=/etc/myapp/env

[Install]
WantedBy=multi-user.target   # Enable karne par multi-user runlevel mein start hoga
```

**Key Directives:**

| Directive | Meaning | Example |
|-----------|---------|---------|
| `User=` / `Group=` | Run process as specific user | `User=www-data` |
| `WorkingDirectory=` | Set working dir before exec | `/var/www` |
| `ExecStart=` | Full command to start | `/usr/bin/python3 app.py` |
| `ExecStop=` | Command to stop (optional) | `/bin/kill $MAINPID` |
| `Restart=` | Restart policy: `no`, `always`, `on-failure` | `on-failure` |
| `RestartSec=` | Seconds to wait before restart | `10` |
| `EnvironmentFile=` | File with env vars (key=value) | `/etc/myapp/env` |
| `After=` / `Requires=` | Dependency ordering | `After=network.target` |
| `Type=` | Service type: `simple`, `forking`, `oneshot`, `notify` | `simple` |

---

### 🧠 3. Zaroorat Kyun Hai?

#### Without systemd unit:
- Application start manually after each reboot → forget → downtime
- Application crash → stays crashed → manual intervention
- Runs as root → security risk
- No logging integration (logs go to systemd journal automatically with unit)

#### With systemd unit:
- `systemctl enable myapp` → starts on boot
- `Restart=on-failure` → auto-restart after crash
- Runs as non-privileged user
- Logs available via `journalctl -u myapp`

---

### ⚠️ 4. Agar Nahi Kiya Toh?

**Scenario:** Tumne ek critical microservice banaya, production mein deploy kiya. Raat ko server reboot hua (kernel update). Subah users complain website down. Tum office aate ho, service manually start karte ho. 4 hours downtime. **Fail.**

---

### ⚙️ 5. Under the Hood (Real Workflow)

**Step 1: Create service user**
```bash
sudo useradd -r -s /usr/sbin/nologin -m -d /opt/myapp appuser
```

**Step 2: Place application in `/opt/myapp`** with correct ownership:
```bash
sudo chown -R appuser:appuser /opt/myapp
```

**Step 3: Create unit file `/etc/systemd/system/myapp.service`**
```ini
[Unit]
Description=My Awesome App
After=network.target

[Service]
Type=simple
User=appuser
Group=appuser
WorkingDirectory=/opt/myapp
ExecStart=/usr/bin/node /opt/myapp/server.js
Restart=on-failure
RestartSec=5
Environment=NODE_ENV=production

[Install]
WantedBy=multi-user.target
```

**Step 4: Reload systemd, enable & start**
```bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
```

**Step 5: Verify**
```bash
systemctl status myapp
journalctl -u myapp -f   # Live logs
```

---

### 🌍 6. Real-World Example

**E-commerce Cart Service:**
- Runs as `cartuser`
- Depends on Redis (`After=redis.service`)
- Auto-restart if fails
- Environment variables from `/etc/cart/env`

```ini
[Unit]
Description=Cart Service
After=network.target redis.service
Requires=redis.service

[Service]
User=cartuser
Group=cartuser
WorkingDirectory=/opt/cart
ExecStart=/usr/bin/java -jar cart.jar
Restart=always
RestartSec=10
EnvironmentFile=/etc/cart/env

[Install]
WantedBy=multi-user.target
```

---

### 🐞 7. Common Mistakes

**Mistake 1:** Forgetting `daemon-reload` after creating/editing unit.
- Changes not picked up → old config used.

**Mistake 2:** Wrong path in `ExecStart` or missing executable permission.
- Service fails to start, status shows error.

**Mistake 3:** Running as root (not setting `User=`).
- Security risk.

**Mistake 4:** `Type=forking` without specifying `PIDFile` correctly.
- Systemd loses track of main process.

**Mistake 5:** Not testing with `systemctl start` before enabling.

---

### ✅ 9. Zaroori Notes for Interview

- **Systemd is PID 1** – manages all services.
- **Enable** = creates symlink in `/etc/systemd/system/multi-user.target.wants/`.
- **Restart policies** – `on-failure` for resilience, `always` for critical daemons.
- **`EnvironmentFile`** – keeps secrets out of unit file.
- **`journalctl -u service`** – primary debugging tool.

**Interview Q&A:**
- Q: How do you ensure a custom app starts on boot and restarts if it crashes?
  A: Create a systemd unit file with `Restart=on-failure`, enable it.
- Q: What's the difference between `systemctl restart` and `systemctl reload`?
  A: Restart stops then starts; reload sends SIGHUP (if supported) without stopping.

---

### ❓ 10. FAQ

**Q1: Unit file edit karne ke baad kya karna zaroori?**
A: `sudo systemctl daemon-reload` – systemd ko naya config batana.

**Q2: `Type=simple` vs `Type=forking`?**
A: Simple – process stays foreground. Forking – process daemonizes; systemd needs PIDFile.

**Q3: Service enable karna aur start karna ek saath kaise?**
A: `sudo systemctl enable --now service` – enable + start ek command mein.

**Q4: Service disable ka matlab?**
A: Boot pe nahi chalega, lekin manual start kar sakte ho.

**Q5: Multiple instances of same service?**
A: Use template units (`@`) – e.g., `myapp@instance1.service`.

---

## 🎯 Topic 14 - Resource Limits (ulimit & Systemd Limits)

### 🐣 1. Simple Analogy

Tumhare paas ek **bada buffet** hai (system resources: files, processes, memory). Har guest (process) ko limit batani zaroori hai – nahi toh ek guest saara khaana khaa jayega aur baaki bhookhe rah jayenge. **Ulimit** = guest ke plate ki size limit.

---

### 📖 2. Technical Definition & What

**ulimit** = user-level resource limits. Shell built-in.

**Types of limits:**

| Limit | Meaning | Example |
|-------|---------|---------|
| `nofile` | Max open file descriptors | `ulimit -n 4096` |
| `nproc` | Max number of processes | `ulimit -u 1024` |
| `maxlogins` | Max concurrent logins | `ulimit -l` (?) |
| `memlock` | Max locked-in-memory | `ulimit -l` |
| `stack` | Stack size | `ulimit -s` |
| `core` | Core file size | `ulimit -c unlimited` |

**Check current limits:**
```bash
ulimit -a
```

**Check limits of a running process:**
```bash
cat /proc/<PID>/limits
```

**Persistent limits (system-wide):** `/etc/security/limits.conf`
```
username soft nofile 4096
username hard nofile 8192
@group soft nproc 512
```

**Systemd unit limits:**
```ini
[Service]
LimitNOFILE=16384
LimitNPROC=512
MemoryMax=2G
CPUQuota=50%
TasksMax=200
```

---

### 🧠 3. Zaroorat Kyun Hai?

**Default limits** (often 1024 open files) are too low for high-traffic servers. Without raising limits:
- Web server (Nginx) rejects new connections with "too many open files"
- Database crashes
- Application can't write logs

---

### ⚠️ 4. Agar Nahi Kiya Toh?

**Scenario:** Black Friday sale, traffic spikes. Nginx hits file descriptor limit (1024). It can't open new connections. Users see "Connection refused". Revenue loss.

---

### ⚙️ 5. Under the Hood (Real Workflow)

**Step 1: Check current limits of nginx**
```bash
pid=$(pgrep -f "nginx: worker" | head -1)
cat /proc/$pid/limits | grep "Max open files"
```

**Step 2: Increase system-wide limit for nginx user**
Edit `/etc/security/limits.conf`:
```
www-data soft nofile 16384
www-data hard nofile 16384
```

**Step 3: For systemd-managed nginx, edit unit override**
```bash
sudo systemctl edit nginx
```
Add:
```
[Service]
LimitNOFILE=16384
```

**Step 4: Restart nginx and verify**
```bash
sudo systemctl restart nginx
cat /proc/$(pgrep -f "nginx: worker" | head -1)/limits
```

---

### 🌍 6. Real-World Example

**MySQL production server:**
- Needs thousands of file descriptors for connections and tables.
- Systemd unit override:
```ini
[Service]
LimitNOFILE=65535
LimitNPROC=65535
```

---

### 🐞 7. Common Mistakes

**Mistake 1:** Setting limits only in shell (`ulimit -n`) – lost after reboot.
**Mistake 2:** Editing `/etc/security/limits.conf` but service is managed by systemd – systemd ignores it unless `User=` in unit and PAM is configured.
**Mistake 3:** Forgetting to restart service after changing limits.

---

### ✅ 9. Zaroori Notes for Interview

- **Hard limit** = absolute ceiling (can't exceed, even by root). **Soft limit** = current limit, can be increased up to hard.
- Systemd limits take precedence for services.
- Always check actual limits with `cat /proc/<PID>/limits`.
- Common high-traffic values: `LimitNOFILE=65535`, `LimitNPROC=65535`.

**Interview Q&A:**
- Q: How would you find out why a process is hitting "too many open files"?
  A: Check current usage with `lsof -p PID | wc -l` and compare with limit from `/proc/PID/limits`.
- Q: How do you permanently increase open file limit for a service?
  A: Use systemd override with `LimitNOFILE=`.

---

### ❓ 10. FAQ

**Q1: ulimit ka effect sirf current session mein kyun hota?**
A: Shell built-in hai, child processes inherit. Reboot ke baad lost.

**Q2: Systemd unit mein `LimitNOFILE` ka syntax?**
A: `LimitNOFILE=soft:hard` ya sirf ek value (soft=hard).

**Q3: What is `tasksmax`?**
A: Max number of tasks (threads) a service can create.

**Q4: Can limits be set per user across all processes?**
A: Yes, via `/etc/security/limits.conf` and PAM.

**Q5: Root user ke limits kyun high hote hain?**
A: Root ko restrictions nahi hoti (usually).

---

## 🎯 Topic 15 - Inodes and Filesystem Structure

### 🐣 1. Simple Analogy

Library mein har book ka ek **catalog card** hota hai – uspar book ka title, author, location likha hota hai. **Inode** = catalog card for a file. File data = actual book. Disk space = library shelves.

Agar catalog cards khatam ho jayen, toh nayi book nahi rakh sakte, chahe shelves khaali hon. **Inode exhaustion** = aisa hi.

---

### 📖 2. Technical Definition & What

**Inode** = data structure storing metadata about a file (except its name):
- File type (regular, dir, symlink, etc.)
- Permissions (rwx)
- Owner (UID/GID)
- Timestamps (atime, mtime, ctime)
- Size
- Pointers to disk blocks where file data lives
- Link count (number of directory entries pointing to this inode)

**Inode table** = array of inodes, created when filesystem is formatted.

**Check inode usage:**
```bash
df -i
```
Output:
```
Filesystem     Inodes  IUsed   IFree IUse% Mounted on
/dev/sda1      655360  450000  205360   69% /
```

**Find directories with many inodes:**
```bash
find / -xdev -type d -exec sh -c 'echo $(ls -a "{}" | wc -l) "{}"' \; | sort -rn | head
```

**Inode number of a file:**
```bash
ls -i file.txt
stat file.txt
```

---

### 🧠 3. Zaroorat Kyun Hai?

Disk space monitoring (`df -h`) only shows blocks, not inodes. If inodes are exhausted:
- Cannot create new files or directories
- Applications fail with "No space left on device" even though `df -h` shows free space
- System may become unstable

---

### ⚠️ 4. Agar Nahi Kiya Toh?

**Scenario:** Mail server stores millions of small emails. Disk usage 60%, but inodes 100% full. New emails cannot be delivered. Postfix fails. Users complain. You check `df -h` – plenty of space! You waste hours troubleshooting permissions, disk space, etc., until you run `df -i`.

---

### ⚙️ 5. Under the Hood

**Create a filesystem with more inodes:**
```bash
mkfs.ext4 -N 1000000 /dev/sdb1   # specify inode count
```

**Find files using inode number:**
```bash
find / -inum 123456
```

**Delete file by inode (if filename has special chars):**
```bash
find . -inum 123456 -delete
```

**Monitor inode usage over time:**
```bash
watch -n 60 'df -i'
```

---

### 🌍 6. Real-World Example

**Docker container running on host with many small temporary files** (e.g., build cache). After months, inodes exhausted on `/var/lib/docker`. Containers fail to start. Solution: cleanup old images (`docker system prune -a`) or recreate filesystem with more inodes.

---

### 🐞 7. Common Mistakes

**Mistake 1:** Only monitoring disk space, not inodes.
**Mistake 2:** Assuming `df -h` gives full picture.
**Mistake 3:** Not cleaning up old logs, mail spools, temp files.

---

### ✅ 9. Zaroori Notes for Interview

- Inode usage is critical for filesystems with many small files.
- `df -i` is your friend.
- Inode count is fixed at filesystem creation (except some filesystems like XFS can grow inode tables).
- Symptoms: "No space left on device" despite free space.

**Interview Q&A:**
- Q: Application fails to write file, `df -h` shows 50% free. What next?
  A: Check `df -i`; likely inode exhaustion.
- Q: How to increase inode count on an existing filesystem?
  A: Generally cannot without reformatting. Some filesystems (XFS) support dynamic inode allocation.

---

### ❓ 10. FAQ

**Q1: Maximum inode count?**
A: Set at mkfs time; ext4 default is 1 inode per 16KB of space (approx).

**Q2: Can inodes be reused after file deletion?**
A: Yes, freed inodes become available for new files.

**Q3: What's the inode number of root directory `/`?**
A: Typically 2 (in ext family).

**Q4: How to see inode of a file?**
A: `ls -i` or `stat`.

**Q5: Symbolic links consume inodes?**
A: Yes, each symlink is a file with its own inode.

---

## 🎯 Topic 16 - Advanced Process Management (htop, iotop, strace)

### 🐣 1. Simple Analogy

- **htop** = CCTV camera with colour coding and zoom – better than old black-and-white `top`.
- **iotop** = See which process is hogging the kitchen sink (disk I/O).
- **strace** = Undercover agent following every system call a process makes – "Oh, he's stuck waiting for a network response."

---

### 📖 2. Technical Definition & What

**htop** – interactive process viewer with scroll, tree view, mouse support, and easy signal sending.
```bash
sudo apt install htop
htop
```
Features:
- F3 search, F4 filter, F5 tree view
- F9 kill menu
- Color-coded CPU/memory bars

**iotop** – shows per-process I/O statistics.
```bash
sudo iotop   # needs root
```
Columns: DISK READ, DISK WRITE, SWAPIN, IO, COMMAND.

**strace** – trace system calls and signals.
```bash
strace -p PID                # trace running process
strace -e open,read command  # trace specific syscalls
strace -o output.txt command # write to file
strace -tt -T                # timestamp + time spent
```

Common syscalls: `open`, `read`, `write`, `connect`, `accept`, `poll`, `select`.

---

### 🧠 3. Zaroorat Kyun Hai?

- `top` is basic; `htop` is much more user-friendly for interactive debugging.
- `iotop` identifies processes causing high disk I/O (e.g., a backup job slowing everything).
- `strace` is the ultimate debugger for "process is stuck" – you can see exactly what it's waiting for (e.g., stuck on `read()` from a socket).

---

### ⚠️ 4. Agar Nahi Kiya Toh?

**Scenario:** Server slow. `top` shows a process at 100% CPU, but you don't know what it's doing. Without `strace`, you guess and maybe kill the wrong process. With `strace -p PID`, you see it's stuck in an infinite loop calling `gettimeofday()` – you identify the bug quickly.

---

### ⚙️ 5. Under the Hood

**Use htop to find culprit:**
- Launch `htop`, press F5 for tree view, see which child process is using CPU.
- Press F9, select signal, kill nicely.

**Use iotop to find disk hog:**
```bash
sudo iotop -o   # only show processes doing I/O
```

**Use strace to debug:**
```bash
# Trace all syscalls of a hung process
sudo strace -p 1234
# If it's stuck on futex (mutex), maybe deadlock.

# Trace file opens of a command
strace -e openat,open cp largefile /backup/
```

**Trace child processes with `-f`** (follow forks).

---

### 🌍 6. Real-World Example

**Mysterious slowdown:** App server slow, CPU low, I/O low. `strace -p` of main process reveals it's stuck on `connect()` to a database that's down. Root cause: DB unreachable, app waiting forever.

---

### 🐞 7. Common Mistakes

**Mistake 1:** Running `strace` on a high-traffic process – generates huge logs, slows it further. Use filters.
**Mistake 2:** Not running `iotop` as root – no I/O stats.
**Mistake 3:** Killing process without understanding root cause.

---

### ✅ 9. Zaroori Notes for Interview

- `htop` is not installed by default, but often available.
- `strace` is invaluable for debugging "stuck" processes.
- `iotop` requires root and CONFIG_TASK_DELAY_ACCT kernel option.

**Interview Q&A:**
- Q: A process is consuming 100% CPU but you can't tell why. How to investigate?
  A: Use `strace -p PID` to see what system calls it's making, or attach with `gdb`.
- Q: How to find which process is writing heavily to disk?
  A: `sudo iotop -o`.

---

### ❓ 10. FAQ

**Q1: `strace` se performance impact?**
A: Huge. Use sparingly, on test/staging if possible.

**Q2: `htop` vs `top`?**
A: `htop` has nicer UI, mouse support, tree view.

**Q3: `iotop` shows 0.00 B/s even when disk busy?**
A: Possibly process is doing direct I/O that bypasses page cache? Or need to check `iotop -a` for accumulated stats.

**Q4: Can `strace` trace already running process?**
A: Yes, with `strace -p PID`.

**Q5: How to trace only network-related syscalls?**
A: `strace -e network -p PID`.

---

## 🎯 Topic 17 - SSH Daemon Hardening (Beyond Permissions)

### 🐣 1. Simple Analogy

Ghar ka **main darwaaza (SSH)** hai. Agar darwaaza weak lock hai, koi bhi andar aa sakta hai. Hardening = darwaaze par multiple strong locks, CCTV, guard.

---

### 📖 2. Technical Definition & What

SSH server config file: `/etc/ssh/sshd_config`

**Key hardening directives:**

| Directive | Recommended Value | Why |
|-----------|-------------------|-----|
| `PermitRootLogin` | `no` | Prevent direct root login (use sudo) |
| `PasswordAuthentication` | `no` | Disable password auth – use SSH keys only |
| `PubkeyAuthentication` | `yes` | Enable key-based auth |
| `AuthorizedKeysFile` | `.ssh/authorized_keys` | Default |
| `X11Forwarding` | `no` | Disable X11 forwarding unless needed |
| `MaxAuthTries` | `3` | Limit login attempts |
| `ClientAliveInterval` | `300` (5 min) | Drop idle connections |
| `ClientAliveCountMax` | `0` | Terminate after first alive check fail |
| `AllowUsers` / `AllowGroups` | specific users/groups | Restrict who can SSH |
| `Protocol` | `2` | Only SSH protocol 2 |
| `Port` | non-22 (e.g., 2222) | Obscurity (not security, but reduces bots) |
| `LogLevel` | `VERBOSE` | Log more details (fingerprints) |

**After changes, restart ssh:**
```bash
sudo systemctl restart sshd
```

---

### 🧠 3. Zaroorat Kyun Hai?

Default SSH config allows password auth and root login. Bots scan the internet constantly trying to brute-force passwords. If a developer uses a weak password, the server can be compromised.

---

### ⚠️ 4. Agar Nahi Kiya Toh?

**Scenario:** Server exposed to internet, `PasswordAuthentication yes`. A bot guesses a weak password for a user (maybe a service account with shell). Attacker gets in, installs crypto miner, steals data.

---

### ⚙️ 5. Under the Hood

**Step 1: Backup current config**
```bash
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup
```

**Step 2: Edit config**
```bash
sudo vim /etc/ssh/sshd_config
```

Set:
```
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
MaxAuthTries 3
ClientAliveInterval 300
ClientAliveCountMax 0
AllowUsers devops john alice
```

**Step 3: Test config syntax**
```bash
sudo sshd -t
```

**Step 4: Reload SSH**
```bash
sudo systemctl reload sshd   # graceful, no downtime
```

---

### 🌍 6. Real-World Example

**Company policy:** Only SSH keys allowed, no passwords. Root login disabled. Developers must use personal accounts with sudo. SSH port changed to 2222 to reduce log noise from bots.

---

### 🐞 7. Common Mistakes

**Mistake 1:** Editing config, forgetting to run `sshd -t`, then restart. Syntax error locks you out!
**Mistake 2:** Setting `PermitRootLogin prohibit-password` still allows root with key; better to disable completely and use sudo.
**Mistake 3:** Changing port without updating firewall – can't connect.
**Mistake 4:** Not having a backup console access (e.g., out-of-band) if SSH config breaks.

---

### ✅ 9. Zaroori Notes for Interview

- Always test config with `sshd -t` before restart.
- Use `AllowUsers` to restrict access to specific users.
- Disable root login and password auth – keys only.
- Change default port only as part of defense-in-depth, not sole security.

**Interview Q&A:**
- Q: How would you harden an SSH server against brute-force attacks?
  A: Disable password auth, use keys, change port, limit users, install fail2ban.
- Q: You changed sshd_config and now can't connect. How to recover?
  A: Use out-of-band console (e.g., AWS EC2 Serial Console) or boot into rescue mode and revert.

---

### ❓ 10. FAQ

**Q1: Password auth band kar di, phir bhi password maang raha?**
A: Check `PubkeyAuthentication` is `yes` and client has correct key.

**Q2: `AllowUsers` vs `AllowGroups`?**
A: `AllowUsers` specific usernames, `AllowGroups` group-based.

**Q3: `ClientAliveInterval` ka matlab?**
A: Server sends alive messages every N seconds; if no response, drops connection.

**Q4: Fail2Ban kya hai?**
A: Tool that watches logs and temporarily bans IPs with too many failed attempts.

**Q5: SSH key passphrase kyun use karna chahiye?**
A: Agar laptop chori ho gaya, passphrase without key use nahi ho sakta (unless attacker also has passphrase). Key alone is insufficient.

---

## 🎯 Topic 18 - Special Permissions (SUID, SGID, Sticky Bit)

### 🐣 1. Simple Analogy

- **SUID** = Jab koi aur tumhara bathroom use kare, to wo tumhara **special pass** use kar sake (program runs with owner's permissions).
- **SGID** = Jab koi group ke shared folder mein file banaye, to wo **group ke hisaab se** ownership mile (group inheritance).
- **Sticky Bit** = Shared fridge mein sab rakh sakte hain, lekin sirf apna hi nikaal sakte ho (delete only by owner).

---

### 📖 2. Technical Definition & What

**Special permission bits** (beyond rwx):

| Bit | Symbolic | Numeric | Effect on file | Effect on directory |
|-----|----------|---------|----------------|---------------------|
| SUID | `s` on user execute | `4xxx` | Runs with file owner's privileges | (ignored on Linux) |
| SGID | `s` on group execute | `2xxx` | Runs with file group's privileges | New files inherit group of directory |
| Sticky | `t` on others execute | `1xxx` | (ignored on Linux) | Only file owner can delete/rename |

**Examples:**
```bash
# SUID on /usr/bin/passwd (owner root)
-rwsr-xr-x 1 root root /usr/bin/passwd
# SGID on directory
drwxrws--- 2 devs project /project
# Sticky on /tmp
drwxrwxrwt 10 root root /tmp
```

**Setting bits:**
```bash
chmod u+s file      # SUID
chmod g+s dir       # SGID on directory
chmod +t dir        # Sticky
chmod 4755 file     # SUID + rwxr-xr-x
```

---

### 🧠 3. Zaroorat Kyun Hai?

- **SUID** allows ordinary users to perform privileged tasks (e.g., `passwd` needs to write `/etc/shadow`).
- **SGID on directories** ensures files created inside a shared directory belong to the correct group, enabling collaboration.
- **Sticky bit** prevents users from deleting others' files in shared temp directories.

---

### ⚠️ 4. Agar Nahi Kiya Toh?

**Scenario (no SGID):** Team shared folder `/projects` owned by group `devs`. User A creates file, group set to A's primary group, not `devs`. User B can't edit. Chaos.

**Scenario (no sticky):** `/tmp` without sticky – any user could delete any other user's temporary files, breaking applications.

---

### ⚙️ 5. Under the Hood

**Find all SUID files (security audit):**
```bash
sudo find / -perm -4000 -type f 2>/dev/null
```

**Find all SGID directories:**
```bash
sudo find / -perm -2000 -type d 2>/dev/null
```

**SGID on directory example:**
```bash
sudo mkdir /projects
sudo chown :devs /projects
sudo chmod 2770 /projects   # rwxrws---, SGID set
# Now any file created inside gets group=devs
```

**Sticky bit example:**
```bash
sudo mkdir /shared
sudo chmod 1777 /shared   # rwxrwxrwt
```

---

### 🌍 6. Real-World Example

**CI/CD agent needs to run with elevated privileges** – instead of running as root, set SUID on a helper binary (though containers are better). But SUID is risky and often avoided.

---

### 🐞 7. Common Mistakes

**Mistake 1:** Setting SUID on shell scripts – kernel ignores SUID on shebang scripts for security reasons. Use compiled binaries.
**Mistake 2:** Leaving SUID on unnecessary binaries – security risk. Regularly audit.
**Mistake 3:** Forgetting SGID on shared directories – leads to permission errors.

---

### ✅ 9. Zaroori Notes for Interview

- SUID = `4`, SGID = `2`, Sticky = `1`.
- SUID on directories ignored in Linux.
- Security: SUID binaries can be exploited if vulnerable; minimize them.
- Sticky bit is why you can't delete another's files in `/tmp`.

**Interview Q&A:**
- Q: What is the sticky bit, and where is it commonly used?
  A: Sticky bit on directories ensures only file owner can delete. Used on `/tmp`.
- Q: How would you find all SUID binaries on a system?
  A: `find / -perm -4000 -type f`.
- Q: Why is SUID on shell scripts dangerous?
  A: Kernel ignores it because of race conditions; also scripts can be manipulated.

---

### ❓ 10. FAQ

**Q1: Numeric representation of SUID+SGID?**
A: `6xxx` (4+2). Example: `6755` = SUID+SGID + rwxr-xr-x.

**Q2: SUID file ka color kyun red hota hai (in ls)?**
A: Default `ls` highlights SUID/SGID in different colors for alert.

**Q3: Can I set SUID on a directory?**
A: Linux ignores it; no effect.

**Q4: Sticky bit directory mein kya effect hota hai?**
A: Users can create files, but only root and file owner can delete/rename.

**Q5: How to remove SUID?**
A: `chmod u-s file` or `chmod 755 file`.

---


## 🎯 Topic 19 - Systemd Resource Control (Cgroups)

### 🐣 1. Simple Analogy

Ek apartment building mein har flat ko **meter** laga do – kitna bijli (CPU), kitna paani (memory) use kar sakta hai. **Cgroups** = Linux ka meter system. **Systemd** = building manager jo meters enforce karta hai.

---

### 📖 2. Technical Definition & What

**Cgroups (control groups)** = Linux kernel feature that limits, accounts for, and isolates resource usage of process groups.

**Systemd integrates cgroups** via unit file directives:

```ini
[Service]
MemoryMax=2G               # Hard memory limit
MemoryHigh=1.5G            # Soft limit, reclaim under pressure
CPUQuota=50%               # Max CPU time (e.g., 50% of one core)
CPUWeight=200               # Relative CPU priority (100 default)
TasksMax=100                # Max number of tasks (threads)
IOWeight=100                # I/O priority
```

**Check current cgroup limits for a service:**
```bash
systemctl show myapp -p MemoryMax,CPUQuota,TasksMax
```

**View cgroup stats:**
```bash
systemd-cgtop
```

---

### 🧠 3. Zaroorat Kyun Hai?

Multi-tenant servers (or even single server with multiple apps) need resource isolation. Without limits:
- One app can consume all memory → OOM killer kills random processes (maybe database).
- One CPU-hungry process can starve others.
- Noisy neighbor problem in shared hosting.

---

### ⚠️ 4. Agar Nahi Kiya Toh?

**Scenario:** Server runs web app and background analytics job. Analytics job has memory leak, consumes all RAM. OOM killer picks the web server process (innocent) and kills it. Site down.

---

### ⚙️ 5. Under the Hood

**Set limits for a systemd service:**
```bash
sudo systemctl set-property myapp MemoryMax=2G CPUQuota=50%
```
This creates a drop-in file in `/etc/systemd/system/myapp.service.d/`.

**Verify:**
```bash
systemctl show myapp -p MemoryMax,CPUQuota
```

**Check actual usage:**
```bash
systemd-cgtop
```

**Example unit with limits:**
```ini
[Service]
MemoryMax=1G
CPUQuota=200%   # two full cores
TasksMax=200
```

---

### 🌍 6. Real-World Example

**Database server (PostgreSQL) on a shared host:**
```ini
[Service]
MemoryMax=8G
CPUQuota=400%   # 4 cores max
IOWeight=1000   # high I/O priority
```

**Sidekiq (background jobs) limited:**
```ini
[Service]
MemoryMax=2G
CPUQuota=100%
TasksMax=50
```

---

### 🐞 7. Common Mistakes

**Mistake 1:** Setting limits too low – service constantly hitting limits, thrashing.
**Mistake 2:** Not monitoring after setting limits – need to ensure application behaves.
**Mistake 3:** Using `MemoryHigh` without `MemoryMax` – soft limit can be exceeded, may still cause OOM.

---

### ✅ 9. Zaroori Notes for Interview

- Cgroups are the underlying mechanism for container runtimes (Docker, containerd).
- Systemd makes cgroups easy to use via unit directives.
- `MemoryMax` = hard limit, process killed if exceeded.
- `CPUQuota` = percentage of CPU time (100% = 1 core).

**Interview Q&A:**
- Q: How do you limit memory usage of a systemd service?
  A: Use `MemoryMax=` in service unit.
- Q: What happens if a process exceeds `MemoryMax`?
  A: OOM killer terminates the process (or kernel may kill it).
- Q: How to see current cgroup stats for a service?
  A: `systemd-cgtop` or `systemctl show`.

---

### ❓ 10. FAQ

**Q1: `MemoryHigh` vs `MemoryMax`?**
A: `MemoryHigh` is a soft limit; kernel tries to reclaim memory, but may exceed. `MemoryMax` is hard limit, never exceeded.

**Q2: Can I set CPU limit per process not using systemd?**
A: Yes, with `cpulimit` or cgroups directly (`cgcreate`, `cgset`), but systemd is easier.

**Q3: Do Docker containers use cgroups?**
A: Yes, Docker relies on cgroups for resource limits.

**Q4: What is `TasksMax`?**
A: Max number of tasks (threads) the service can create.

**Q5: How to set I/O limit?**
A: `IOWeight` for relative priority, or `IODeviceWeight` for specific devices.

---

## 🎯 Topic 20 - Kernel Tuning & Sysctl

### 🐣 1. Simple Analogy

Linux kernel = **car engine**. Default settings = factory tune – good for general driving. But for racing (high traffic), you need to **tweak** – fuel mix, turbo boost. **Sysctl** = tuning knobs.

---

### 📖 2. Technical Definition & What

**sysctl** = interface to read and modify kernel parameters at runtime.

Parameters live under `/proc/sys/`. For example, `/proc/sys/net/core/somaxconn`.

**View all parameters:**
```bash
sysctl -a
```

**Temporary change:**
```bash
sysctl -w net.core.somaxconn=1024
```

**Permanent changes:** add to `/etc/sysctl.conf` or `/etc/sysctl.d/99-tuning.conf`.
```
net.core.somaxconn = 1024
net.ipv4.tcp_tw_reuse = 1
vm.swappiness = 10
```

**Apply changes:**
```bash
sysctl -p
```

---

### 🧠 3. Zaroorat Kyun Hai?

Default kernel parameters are conservative. High-traffic servers need tuning for:
- More concurrent connections (`somaxconn`, `tcp_tw_reuse`)
- Handle more file descriptors (`fs.file-max`)
- Better memory management (`vm.swappiness`)
- Network performance (`net.core.rmem_max`, `net.core.wmem_max`)

---

### ⚠️ 4. Agar Nahi Kiya Toh?

**Scenario:** Web server under load, connections drop with "connection refused" even though CPU low. Reason: `net.core.somaxconn` default 128 too low for high backlog.

---

### ⚙️ 5. Under the Hood

**Common production sysctl tweaks:**

```bash
# Increase max open files (system-wide)
fs.file-max = 2097152

# Increase network buffer sizes
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216
net.ipv4.tcp_rmem = 4096 87380 16777216
net.ipv4.tcp_wmem = 4096 65536 16777216

# Enable TCP fast recycling (use with caution)
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_tw_recycle = 0   # don't enable, can cause NAT issues

# Increase backlog
net.core.somaxconn = 65535
net.ipv4.tcp_max_syn_backlog = 65535

# Lower swappiness (prefer to use RAM over swap)
vm.swappiness = 10

# Increase local port range for outgoing connections
net.ipv4.ip_local_port_range = 10240 65535
```

**Verify after applying:**
```bash
sysctl net.core.somaxconn
```

---

### 🌍 6. Real-World Example

**High-traffic Nginx server tuning:**
```bash
# /etc/sysctl.d/99-nginx.conf
net.core.somaxconn = 65535
net.ipv4.tcp_max_syn_backlog = 65535
net.ipv4.tcp_tw_reuse = 1
fs.file-max = 2097152
```

**Database server (MySQL) tuning:**
```bash
vm.swappiness = 1
vm.dirty_ratio = 30
vm.dirty_background_ratio = 5
```

---

### 🐞 7. Common Mistakes

**Mistake 1:** Applying network tweaks without understanding – e.g., `tcp_tw_recycle` breaks NAT.
**Mistake 2:** Not testing in staging – may cause instability.
**Mistake 3:** Forgetting to persist changes – reboot loses them.
**Mistake 4:** Over-tuning – diminishing returns, may cause unexpected issues.

---

### ✅ 9. Zaroori Notes for Interview

- Sysctl controls kernel parameters.
- Common high-traffic parameters: `somaxconn`, `tcp_tw_reuse`, `ip_local_port_range`, `fs.file-max`.
- Persist changes in `/etc/sysctl.conf` or `/etc/sysctl.d/`.
- Test thoroughly in non-production.

**Interview Q&A:**
- Q: Our application is making many outbound connections and fails with "Cannot assign requested address". Which sysctl would you check?
  A: `net.ipv4.ip_local_port_range` – increase the range.
- Q: What does `vm.swappiness` control?
  A: Tendency to swap out anonymous memory. Lower = prefer RAM.

---

### ❓ 10. FAQ

**Q1: `tcp_tw_reuse` kya karta hai?**
A: Allows reusing TIME_WAIT sockets for new connections (safe in many cases).

**Q2: `net.core.somaxconn` ka default kya hai?**
A: Usually 128. For high traffic, increase to 1024 or more.

**Q3: Change temporary vs permanent?**
A: `sysctl -w` temporary; add to `.conf` for permanent.

**Q4: Sysctl changes require reboot?**
A: No, `sysctl -p` applies immediately.

**Q5: Where to find all tunable parameters?**
A: `sysctl -a` and kernel docs.

---

