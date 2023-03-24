<!--
Please fill this template entirely and do not erase parts of it.
We reserve the right to close without a response
bug reports which are incomplete.
-->
# Checklist
<!--
To check an item on the list replace [ ] with [x].
-->
- [ ] I have verified that the issue exists against the `main` branch of Celery.
- [ ] This has already been asked to the [discussions forum](https://github.com/celery/celery/discussions) first.
- [ ] I have read the relevant section in the
  [contribution guide](https://docs.celeryq.dev/en/main/contributing.html#other-bugs)
  on reporting bugs.
- [ ] I have checked the [issues list](https://github.com/celery/celery/issues?q=is%3Aissue+label%3A%22Issue+Type%3A+Bug+Report%22+-label%3A%22Category%3A+Documentation%22)
  for similar or identical bug reports.
- [ ] I have checked the [pull requests list](https://github.com/celery/celery/pulls?q=is%3Apr+label%3A%22PR+Type%3A+Bugfix%22+-label%3A%22Category%3A+Documentation%22)
  for existing proposed fixes.
- [ ] I have checked the [commit log](https://github.com/celery/celery/commits/main)
  to find out if the bug was already fixed in the main branch.
- [ ] I have included all related issues and possible duplicate issues
  in this issue (If there are none, check this box anyway).

## Mandatory Debugging Information

- [ ] I have included the output of ``celery -A proj report`` in the issue.
    (if you are not able to do this, then at least specify the Celery
     version affected).
- [ ] I have verified that the issue exists against the `main` branch of Celery.
- [ ] I have included the contents of ``pip freeze`` in the issue.
- [ ] I have included all the versions of all the external dependencies required
  to reproduce this bug.

## Optional Debugging Information
<!--
Try some of the below if you think they are relevant.
It will help us figure out the scope of the bug and how many users it affects.
-->
- [ ] I have tried reproducing the issue on more than one Python version
  and/or implementation.
- [ ] I have tried reproducing the issue on more than one message broker and/or
  result backend.
- [ ] I have tried reproducing the issue on more than one version of the message
  broker and/or result backend.
- [ ] I have tried reproducing the issue on more than one operating system.
- [ ] I have tried reproducing the issue on more than one workers pool.
- [ ] I have tried reproducing the issue with autoscaling, retries,
  ETA/Countdown & rate limits disabled.
- [ ] I have tried reproducing the issue after downgrading
  and/or upgrading Celery and its dependencies.

## Related Issues and Possible Duplicates
<!--
Please make sure to search and mention any related issues
or possible duplicates to this issue as requested by the checklist above.

This may or may not include issues in other repositories that the Celery project
maintains or other repositories that are dependencies of Celery.

If you don't know how to mention issues, please refer to Github's documentation
on the subject: https://help.github.com/en/articles/autolinked-references-and-urls#issues-and-pull-requests
-->

#### Related Issues

- None

#### Possible Duplicates

- None

## Environment & Settings
<!-- Include the contents of celery --version below -->
**Celery version**:
<!-- Include the output of celery -A proj report below -->
<details>
<summary><b><code>celery report</code> Output:</b></summary>
<p>

```
```

</p>
</details>

# Steps to Reproduce

## Required Dependencies
<!-- Please fill the required dependencies to reproduce this issue -->
- **Minimal Python Version**: N/A or Unknown
- **Minimal Celery Version**: N/A or Unknown
- **Minimal Kombu Version**: N/A or Unknown
- **Minimal Broker Version**: N/A or Unknown
- **Minimal Result Backend Version**: N/A or Unknown
- **Minimal OS and/or Kernel Version**: N/A or Unknown
- **Minimal Broker Client Version**: N/A or Unknown
- **Minimal Result Backend Client Version**: N/A or Unknown

### Python Packages
<!-- Please fill the contents of pip freeze below -->
<details>
<summary><b><code>pip freeze</code> Output:</b></summary>
<p>

```
```

</p>
</details>

### Other Dependencies
<!--
Please provide system dependencies, configuration files
and other dependency information if applicable
-->
<details>
<p>
N/A
</p>
</details>

## Minimally Reproducible Test Case
<!--
Please provide a reproducible test case.
Refer to the Reporting Bugs section in our contribution guide.

We prefer submitting test cases in the form of a PR to our integration test suite.
If you can provide one, please mention the PR number below.
If not, please attach the most minimal code example required to reproduce the issue below.
If the test case is too large, please include a link to a gist or a repository below.
-->

<details>
<p>

```python
```

</p>
</details>

# Expected Behavior
<!-- Describe in detail what you expect to happen -->

# Actual Behavior
<!--
Describe in detail what actually happened.
Please include a backtrace and surround it with triple backticks (```).
In addition, include the Celery daemon logs, the broker logs,
the result backend logs and system logs below if they will help us debug
the issue.
-->

```
9:12 2023-03-23 11:29:12.494461+00:00 [warning] <0.7157.0> closing AMQP connection <0.7157.0> (172.21.0.1:40340 -> 172.21.0.2:5672, vhost: '/', user: 'guest'):
2023-03-23 17:29:12 2023-03-23 11:29:12.494461+00:00 [warning] <0.7157.0> client unexpectedly closed TCP connection
2023-03-23 17:29:12 2023-03-23 11:29:12.494826+00:00 [warning] <0.7144.0> closing AMQP connection <0.7144.0> (172.21.0.1:40338 -> 172.21.0.2:5672, vhost: '/', user: 'guest'):
2023-03-23 17:29:12 2023-03-23 11:29:12.494826+00:00 [warning] <0.7144.0> client unexpectedly closed TCP connection
2023-03-23 17:29:12 2023-03-23 11:29:12.495011+00:00 [warning] <0.7133.0> closing AMQP connection <0.7133.0> (172.21.0.1:40336 -> 172.21.0.2:5672, vhost: '/', user: 'guest'):
2023-03-23 17:29:12 2023-03-23 11:29:12.495011+00:00 [warning] <0.7133.0> client unexpectedly closed TCP connection
2023-03-23 17:31:48 2023-03-23 11:31:48.198138+00:00 [error] <0.7186.0> closing AMQP connection <0.7186.0> (172.21.0.1:41422 -> 172.21.0.2:5672):
2023-03-23 17:31:48 2023-03-23 11:31:48.198138+00:00 [error] <0.7186.0> missed heartbeats from client, timeout: 60s
```

```
  warnings.warn(SecurityWarning(ROOT_DISCOURAGED.format(
[2023-03-23 11:20:48,084: DEBUG/MainProcess] | Worker: Preparing bootsteps.
[2023-03-23 11:20:48,086: DEBUG/MainProcess] | Worker: Building graph...
[2023-03-23 11:20:48,086: DEBUG/MainProcess] | Worker: New boot order: {Beat, StateDB, Timer, Hub, Pool, Autoscaler, Consumer}
[2023-03-23 11:20:48,144: DEBUG/MainProcess] | Consumer: Preparing bootsteps.
[2023-03-23 11:20:48,145: DEBUG/MainProcess] | Consumer: Building graph...
[2023-03-23 11:20:48,151: DEBUG/MainProcess] | Consumer: New boot order: {Connection, Events, Heart, CrawlerConsumerStep, Agent, Mingle, Tasks, Control, Gossip, event loop}

 -------------- celery@kind-control-plane v5.2.7 (dawn-chorus)
--- ***** -----
-- ******* ---- Linux-5.10.16.3-microsoft-standard-WSL2-x86_64-with-glibc2.2.5 2023-03-23 11:20:48
- *** --- * ---
- ** ---------- [config]
- ** ---------- .> app:         proj:0x7f4e3e7debb0
- ** ---------- .> transport:   amqp://guest:**@host.docker.internal:5672//
- ** ---------- .> results:     disabled://
- *** --- * --- .> concurrency: 1 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** -----
[2023-03-23 11:20:48,199: DEBUG/MainProcess] using channel_id: 1
[2023-03-23 11:20:48,201: DEBUG/MainProcess] Channel open
[2023-03-23 11:20:48,257: DEBUG/MainProcess] ^-- substep ok
[2023-03-23 11:20:48,257: DEBUG/MainProcess] | Consumer: Starting Tasks
[2023-03-23 11:20:48,259: DEBUG/MainProcess] using channel_id: 2
[2023-03-23 11:20:48,261: DEBUG/MainProcess] Channel open
[2023-03-23 11:20:48,266: DEBUG/MainProcess] ^-- substep ok
[2023-03-23 11:20:48,199: DEBUG/MainProcess] using channel_id: 1
[2023-03-23 11:20:48,201: DEBUG/MainProcess] Channel open
[2023-03-23 11:20:48,257: DEBUG/MainProcess] ^-- substep ok
[2023-03-23 11:20:48,257: DEBUG/MainProcess] | Consumer: Starting Tasks
[2023-03-23 11:20:48,259: DEBUG/MainProcess] using channel_id: 2
[2023-03-23 11:20:48,261: DEBUG/MainProcess] Channel open
[2023-03-23 11:20:48,266: DEBUG/MainProcess] ^-- substep ok
[2023-03-23 11:20:48,267: DEBUG/MainProcess] | Consumer: Starting Control
[2023-03-23 11:20:48,267: DEBUG/MainProcess] using channel_id: 3
[2023-03-23 11:20:48,268: DEBUG/MainProcess] Channel open
[2023-03-23 11:20:48,277: DEBUG/MainProcess] ^-- substep ok
[2023-03-23 11:20:48,277: DEBUG/MainProcess] | Consumer: Starting event loop
[2023-03-23 11:20:48,278: DEBUG/MainProcess] | Worker: Hub.register Pool...
[2023-03-23 11:20:48,280: WARNING/MainProcess] /usr/local/lib/python3.8/site-packages/celery/fixups/django.py:203: UserWarning: Using settings.DEBUG leads to a memory                            leak, never use this setting in production environments!
  warnings.warn('''Using settings.DEBUG leads to a memory
                                                                                                                                                                                      [2023-03-23 11:20:48,280: INFO/MainProcess] celery@kind-control-plane ready.
[2023-03-23 11:20:48,280: DEBUG/MainProcess] basic.qos: prefetch_count->4
[2023-03-23 11:21:08,281: DEBUG/MainProcess] heartbeat_tick : for connection c732ca02ed0a42d28a6cc25477d027f4                                                                         [2023-03-23 11:21:08,281: DEBUG/MainProcess] heartbeat_tick : Prev sent/recv: None/None, now - 20/20, monotonic - 28316.1393052, last_heartbeat_sent - 28316.13929, heartbeat int. - 60 for connection c732ca02ed0a42d28a6cc25477d027f4
[2023-03-23 11:21:28,288: DEBUG/MainProcess] heartbeat_tick : for connection c732ca02ed0a42d28a6cc25477d027f4                                                                         [2023-03-23 11:21:28,288: DEBUG/MainProcess] heartbeat_tick : Prev sent/recv: 20/20, now - 20/21, monotonic - 28336.1455468, last_heartbeat_sent - 28316.13929, heartbeat int. - 60 for connection c732ca02ed0a42d28a6cc25477d027f4
[2023-03-23 11:21:48,288: DEBUG/MainProcess] heartbeat_tick : for connection c732ca02ed0a42d28a6cc25477d027f4
[2023-03-23 11:21:48,288: DEBUG/MainProcess] heartbeat_tick : Prev sent/recv: 20/21, now - 20/22, monotonic - 28356.1462088, last_heartbeat_sent - 28316.13929, heartbeat int. - 60 for connection c732ca02ed0a42d28a6cc25477d027f4
[2023-03-23 11:22:08,295: DEBUG/MainProcess] heartbeat_tick : for connection c732ca02ed0a42d28a6cc25477d027f4
[2023-03-23 11:22:08,295: DEBUG/MainProcess] heartbeat_tick : Prev sent/recv: 20/22, now - 20/22, monotonic - 28376.1525458, last_heartbeat_sent - 28316.13929, heartbeat int. - 60 for connection c732ca02ed0a42d28a6cc25477d027f4
[2023-03-23 11:22:08,295: DEBUG/MainProcess] heartbeat_tick: sending heartbeat for connection c732ca02ed0a42d28a6cc25477d027f4
[2023-03-23 11:22:28,298: DEBUG/MainProcess] heartbeat_tick : for connection c732ca02ed0a42d28a6cc25477d027f4                                                                         [2023-03-23 11:22:28,298: DEBUG/MainProcess] heartbeat_tick : Prev sent/recv: 20/22, now - 21/23, monotonic - 28396.1556637, last_heartbeat_sent - 28396.1556626, heartbeat int. - 60 for connection c732ca02ed0a42d28a6cc25477d027f4
[2023-03-23 11:22:48,299: DEBUG/MainProcess] heartbeat_tick : for connection c732ca02ed0a42d28a6cc25477d027f4
[2023-03-23 11:22:48,299: DEBUG/MainProcess] heartbeat_tick : Prev sent/recv: 21/23, now - 21/24, monotonic - 28416.157091, last_heartbeat_sent - 28396.1556626, heartbeat int. - 60 for connection c732ca02ed0a42d28a6cc25477d027f4
[2023-03-23 11:23:08,305: DEBUG/MainProcess] heartbeat_tick : for connection c732ca02ed0a42d28a6cc25477d027f4
[2023-03-23 11:23:08,305: DEBUG/MainProcess] heartbeat_tick : Prev sent/recv: 21/24, now - 21/24, monotonic - 28436.1627791, last_heartbeat_sent - 28396.1556626, heartbeat int. - 60 for connection c732ca02ed0a42d28a6cc25477d027f4
[2023-03-23 11:23:28,308: DEBUG/MainProcess] heartbeat_tick : for connection c732ca02ed0a42d28a6cc25477d027f4
[2023-03-23 11:23:28,308: DEBUG/MainProcess] heartbeat_tick : Prev sent/recv: 21/24, now - 21/25, monotonic - 28456.1661616, last_heartbeat_sent - 28396.1556626, heartbeat int. - 60 for connection c732ca02ed0a42d28a6cc25477d027f4
[2023-03-23 11:23:28,308: DEBUG/MainProcess] heartbeat_tick: sending heartbeat for connection c732ca02ed0a42d28a6cc25477d027f4
[2023-03-23 11:23:48,309: DEBUG/MainProcess] heartbeat_tick : for connection c732ca02ed0a42d28a6cc25477d027f4
[2023-03-23 11:23:48,309: DEBUG/MainProcess] heartbeat_tick : Prev sent/recv: 21/25, now - 22/26, monotonic - 28476.1669342, last_heartbeat_sent - 28476.1669334, heartbeat int. - 60 for connection c732ca02ed0a42d28a6cc25477d027f4
[2023-03-23 11:24:08,315: DEBUG/MainProcess] heartbeat_tick : for connection c732ca02ed0a42d28a6cc25477d027f4
[2023-03-23 11:24:08,315: DEBUG/MainProcess] heartbeat_tick : Prev sent/recv: 22/26, now - 22/26, monotonic - 28496.1725562, last_heartbeat_sent - 28476.1669334, heartbeat int. - 60 for connection c732ca02ed0a42d28a6cc25477d027f4
[2023-03-23 11:24:28,316: DEBUG/MainProcess] heartbeat_tick : for connection c732ca02ed0a42d28a6cc25477d027f4
[2023-03-23 11:24:28,316: DEBUG/MainProcess] heartbeat_tick : Prev sent/recv: 22/26, now - 22/27, monotonic - 28516.1745252, last_heartbeat_sent - 28476.1669334, heartbeat int. - 60 for connection c732ca02ed0a42d28a6cc25477d027f4
[2023-03-23 11:24:48,317: DEBUG/MainProcess] heartbeat_tick : for connection c732ca02ed0a42d28a6cc25477d027f4
for connection c732ca02ed0a42d28a6cc25477d027f4
[2023-03-23 11:28:48,360: DEBUG/MainProcess] heartbeat_tick: sending heartbeat for connection c732ca02ed0a42d28a6cc25477d027f4
[2023-03-23 11:29:08,366: DEBUG/MainProcess] heartbeat_tick : for connection c732ca02ed0a42d28a6cc25477d027f4
[2023-03-23 11:29:08,366: DEBUG/MainProcess] heartbeat_tick : Prev sent/recv: 25/36, now - 26/36, monotonic - 28796.2235417, last_heartbeat_sent - 28796.2235402, heartbeat int. - 60 for connection c732ca02ed0a42d28a6cc25477d027f4INFO: [2023-03-23 11:29:12] /usr/src/app/proj/celery.py:90 handle_message message=<Message object at 0x7f4e3d3f2310 with details {'state': 'RECEIVED', 'content_type': 'application/json', 'delivery_tag': 1, 'body_length': 13, 'properties': {}, 'delivery_info': {'exchange': 'test_exchange', 'routing_key': 'test'}}>message_routing_key='test'
params={'wait': 360}[2023-03-23 11:29:12,507: INFO/MainProcess] message=<Message object at 0x7f4e3d3f2310 with details {'state': 'RECEIVED', 'content_type': 'application/json', 'delivery_tag': 1, 'body_length': 13, 'properties': {}, 'delivery_info': {'exchange': 'test_exchange', 'routing_key': 'test'}}>message_routing_key='test'
params={'wait': 360}INFO: [2023-03-23 11:35:12] /usr/src/app/proj/celery.py:90 handle_message message=<Message object at 0x7f4e3d3f2160 with details {'state': 'RECEIVED', 'content_type': 'application/json', 'delivery_tag': 2, 'body_length': 13, 'properties': {}, 'delivery_info': {'exchange': 'test_exchange', 'routing_key': 'test'}}>
message_routing_key='test'
params={'wait': 360}[2023-03-23 11:35:12,567: INFO/MainProcess] message=<Message object at 0x7f4e3d3f2160 with details {'state': 'RECEIVED', 'content_type': 'application/json', 'delivery_tag': 2, 'body_length': 13, 'properties': {}, 'delivery_info': {'exchange': 'test_exchange', 'routing_key': 'test'}}>
message_routing_key='test'params={'wait': 360}
[2023-03-23 11:41:12,668: DEBUG/MainProcess] heartbeat_tick : for connection c732ca02ed0a42d28a6cc25477d027f4[2023-03-23 11:41:12,668: DEBUG/MainProcess] heartbeat_tick : Prev sent/recv: 26/36, now - 28/42, monotonic - 29520.5260476, last_heartbeat_sent - 29520.5260458, heartbeat int. - 60 for connection c732ca02ed0a42d28a6cc25477d027f4INFO: [2023-03-23 11:41:12] /usr/src/app/proj/celery.py:90 handle_message message=<Message object at 0x7f4e3d3f23a0 with details {'state': 'RECEIVED', 'content_type': 'application/json', 'delivery_tag': 3, 'body_length': 13, 'properties': {}, 'delivery_info': {'exchange': 'test_exchange', 'routing_key': 'test'}}>message_routing_key='test'params={'wait': 360}[2023-03-23 11:41:12,668: INFO/MainProcess] message=<Message object at 0x7f4e3d3f23a0 with details {'state': 'RECEIVED', 'content_type': 'application/json', 'delivery_tag': 3, 'body_length': 13, 'properties': {}, 'delivery_info': {'exchange': 'test_exchange', 'routing_key': 'test'}}>
message_routing_key='test'params={'wait': 360}
```
