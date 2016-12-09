#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#
from com.xebialabs.deployit.engine.api.execution import TaskExecutionState

def test_check_connection_organization_success():
    server = repository.read('Infrastructure/XebiaLabs')
    control = deployit.prepareControlTask(server, 'CheckConnection')
    task_id = deployit.createControlTask(control)
    deployit.startTaskAndWait(task_id)
    assert TaskExecutionState.DONE == task2.get(task_id).state

def test_check_connection_space_success():
    server = repository.read('Infrastructure/XebiaLabs/XLR')
    control = deployit.prepareControlTask(server, 'CheckConnection')
    task_id = deployit.createControlTask(control)
    deployit.startTaskAndWait(task_id)
    assert TaskExecutionState.DONE == task2.get(task_id).state