# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RoaRequest

class GetResourcePodsRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'eas', '2018-05-22', 'GetResourcePods')
		self.set_uri_pattern('/api/resources/[cluster_id]/[resource_name]/instances/[instance_name]/pods')
		self.set_method('GET')

	def get_cluster_id(self):
		return self.get_path_params().get('cluster_id')

	def set_cluster_id(self,cluster_id):
		self.add_path_param('cluster_id',cluster_id)

	def get_instance_name(self):
		return self.get_path_params().get('instance_name')

	def set_instance_name(self,instance_name):
		self.add_path_param('instance_name',instance_name)

	def get_resource_name(self):
		return self.get_path_params().get('resource_name')

	def set_resource_name(self,resource_name):
		self.add_path_param('resource_name',resource_name)