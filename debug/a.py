import os; import shutil; import subprocess; command = shutil.which("python"); args = [command, "debug/s.py"]
env = os.environ.copy(); env["CUMULUSCI_KEYCHAIN_CLASS"] = "cumulusci.core.keychain.EnvironmentProjectKeychain"; env["CUMULUSCI_SCRATCH_ORG_CLASS"] = "cumulusci.core.config.OrgConfig"; env["CUMULUSCI_DISABLE_REFRESH"] = "1"
p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE, close_fds=True, env=env, cwd='/app')
orig_stdout, _ = p.communicate(); print(orig_stdout)