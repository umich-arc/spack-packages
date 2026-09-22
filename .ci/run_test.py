import os

from globus_compute_sdk import Executor
from globus_compute_sdk.serialize import ComputeSerializer, JSONData, PureSourceDill

endpoint_id = "8c7f597d-af89-4af0-b4b5-75619ef793f1"


def func():
    import pytest

    return pytest.main(["-v", "--exitfirst"])


with Executor(
    endpoint_id=endpoint_id,
    user_endpoint_config={"commit_sha": os.environ["COMMIT_SHA"]},
) as ex:
    ex.serializer = ComputeSerializer(strategy_code=PureSourceDill, strategy_data=JSONData)
    fut = ex.submit(func)
    res = fut.result()

print(res)
# ADD RESULT PROCESSING LOGIC
