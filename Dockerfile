# 
# Copyright 2015 Stefano Terna
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 

FROM ubuntu:latest
MAINTAINER iottly

EXPOSE 8521

RUN apt-get update -y

RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential
RUN apt-get install -y python python-dev python-distribute python-pip

RUN mkdir /iottly-client-core

ADD requirements.txt /iottly-client-core/requirements.txt
RUN pip install -r /iottly-client-core/requirements.txt

ADD run_script.sh /iottly-client-core/run_script.sh
ADD /iottly_client_core /iottly-client-core/iottly_client_core

WORKDIR /iottly-client-core
CMD ["./run_script.sh", "iottly_client_core/main.py"] 