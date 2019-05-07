#
# Copyright 2019 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from com.xebialabs.deployit.engine.api.execution import TaskExecutionState

def check_control_task(infrastructure_id, control_task, expected_final_state):
    server = repository.read(infrastructure_id)
    control = deployit.prepareControlTask(server, control_task)
    task_id = deployit.createControlTask(control)
    deployit.startTaskAndWait(task_id)
    assert task2.get(task_id).state == expected_final_state

def test_discover_spaces_success():
    check_control_task(
        'Infrastructure/XebiaLabs',
        'DiscoverSpaces',
        TaskExecutionState.DONE
    )

def test_discover_domains_success():
    check_control_task(
        'Infrastructure/XebiaLabs',
        'DiscoverDomains',
        TaskExecutionState.DONE
    )

def test_check_connection_organization_success():
    check_control_task(
        'Infrastructure/XebiaLabs',
        'CheckConnection',
        TaskExecutionState.DONE
    )

def test_check_connection_space_success():
    check_control_task(
        'Infrastructure/XebiaLabs/XLR',
        'CheckConnection',
        TaskExecutionState.DONE
    )
