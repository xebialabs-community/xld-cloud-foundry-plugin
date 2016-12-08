#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#
from com.xebialabs.deployit.engine.api.execution import TaskExecutionState

def test_discover_spaces_success():
    server = repository.read('Infrastructure/XebiaLabs')
    control = deployit.prepareControlTask(server, 'DiscoverSpaces')
    task_id = deployit.createControlTask(control)
    deployit.startTaskAndWait(task_id)
    assert TaskExecutionState.DONE == task2.get(task_id).state

def test_discover_domains_success():
    server = repository.read('Infrastructure/XebiaLabs')
    control = deployit.prepareControlTask(server, 'DiscoverDomains')
    task_id = deployit.createControlTask(control)
    deployit.startTaskAndWait(task_id)
    assert TaskExecutionState.DONE == task2.get(task_id).state