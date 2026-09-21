from globus_compute_sdk import Executor, ShellFunction

endpoint_id = "8c7f597d-af89-4af0-b4b5-75619ef793f1"

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
