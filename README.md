# License

Copyright 2015 Stefano Terna

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

# iottly-client-core
The *iottly-client-core* repo hosts a template project for a client Iottly application.
Iottly decouples IoT development in two main phases:
- IoT communication and device programming, which is Iottly core
- IoT end user interface and functions developmnent, which needs to be customizes on a per project basis.

You can use this template to build custom end user interfaces and functions running on top of Iottly.

It performs the following main functions:
- it receives incoming messages from devices, on `/msg` handler, via the [iottly-core](https://github.com/iottly/iottly-core) client callback functionality
- it provides a basic frontend interface to the developers, [iottly-client-UI](https://github.com/iottly/iottly-client-UI)
- it pushes messages to the [iottly-client-UI](https://github.com/iottly/iottly-client-UI) in real-time, via websockets


# Setup instructions

Please refer to [Iottly docker](https://github.com/iottly/iottly-docker) for prerequisites and full Iottly setup.
