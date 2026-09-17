from globus_compute_sdk import Executor, ShellFunction

endpoint_id = "aed92014-81b1-44b7-b82a-68b21feeff44"

func = ShellFunction("spack audit packages", return_dict=True)
with Executor(
    endpoint_id=endpoint_id,
    user_endpoint_config={
        "OPTIONS": "--time 30",
        "COMMAND": "source /sw/spack/arc/spack/share/spack/setup-env.sh",
    },
) as ex:
    fut = ex.submit(func)
    res = fut.result()

# ADD RESULT PROCESSING LOGIC
