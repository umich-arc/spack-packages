from globus_compute_sdk import Executor, ShellFunction

endpoint_id = "113871fa-ecc5-4b54-af3a-1b5b0e7206bf"

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
