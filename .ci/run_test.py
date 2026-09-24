import os
import sys

from globus_compute_sdk import Executor
from globus_compute_sdk.serialize import ComputeSerializer, JSONData, PureSourceDill

endpoint_id = "8c7f597d-af89-4af0-b4b5-75619ef793f1"


def func():
    import os

    import pytest

    working_dir = os.environ["WORKDIR"] + "/" + "spack-packages"
    os.chdir(working_dir)
    return pytest.main(["-v", "--exitfirst"])


with Executor(
    endpoint_id=endpoint_id,
    user_endpoint_config={
        "commit_sha": os.environ["COMMIT_SHA"],
        "gh_token": os.environ["GH_TOKEN"],
        "run_id": os.environ["GITHUB_RUN_ID"] + "." + os.environ["GITHUB_RUN_ATTEMPT"],
    },
) as ex:
    ex.serializer = ComputeSerializer(strategy_code=PureSourceDill, strategy_data=JSONData)
    fut = ex.submit(func)
    res = fut.result()

sys.exit(res)
# ADD RESULT PROCESSING LOGIC
