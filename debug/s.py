import logging 
import os 
import shutil
import subprocess

logger = logging.getLogger(__name__)

def run_flow(): 
    """Run a flow on a scratch org"""
    # Run flow in a subprocess so we can control the environment
    project_path = '/app'
    command = shutil.which("robot")
    args = [command, "/app/debug/test.robot"]
    env = {
        "HOME": project_path,
        "PATH": os.environ["PATH"],
        "NEOCOL_TEST": os.environ.get("NEOCOL_TEST"),
        "NEOCOL_UNLOCKED_PACKAGE_PASSWORD_FOR_ASYNC_ACTION_FRAMEWORK_V1": os.environ.get("NEOCOL_UNLOCKED_PACKAGE_PASSWORD_FOR_ASYNC_ACTION_FRAMEWORK_V1"),
        "NEOCOL_UNLOCKED_PACKAGE_PASSWORD_FOR_COMMON_UTILITIES_P1": os.environ.get("NEOCOL_UNLOCKED_PACKAGE_PASSWORD_FOR_COMMON_UTILITIES_P1"),
        "NEOCOL_UNLOCKED_PACKAGE_PASSWORD_FOR_CUSTOM_SCHEDULES_P1": os.environ.get("NEOCOL_UNLOCKED_PACKAGE_PASSWORD_FOR_CUSTOM_SCHEDULES_P1"),
        "NEOCOL_UNLOCKED_PACKAGE_PASSWORD_FOR_CPQ_CALM_CONNECTOR_P1": os.environ.get("NEOCOL_UNLOCKED_PACKAGE_PASSWORD_FOR_CPQ_CALM_CONNECTOR_P1"),
        "NEOCOL_UNLOCKED_PACKAGE_PASSWORD_FOR_STRIPE_HOSTED_PAYMENT_PAGE_P1": os.environ.get("NEOCOL_UNLOCKED_PACKAGE_PASSWORD_FOR_STRIPE_HOSTED_PAYMENT_PAGE_P1"),
        "PYTHONPATH": os.environ.get("PYTHONPATH"),
        "LD_LIBRARY_PATH": os.environ.get("LD_LIBRARY_PATH"),
        "LIBRARY_PATH": os.environ.get("LIBRARY_PATH")
    }

    p = subprocess.Popen(
        args,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        stdin=subprocess.PIPE,
        close_fds=True,
        env=env,
        cwd=project_path,
    )
    orig_stdout, _ = p.communicate()
    print(orig_stdout)