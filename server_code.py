from generated_automatically import test_pb2, test_pb2_grpc

class testing(test_pb2_grpc.test_grpcServicer):
	def test_function(self, request, context):
		if request.number == 0:
			answer = "false"
		else:
			answer = "true"
		return test_pb2.output(status=answer)
		
	def test_second_function(self, request, context):
		if request.number == 0:
			answer = "The number is 0"
		else:
			answer = "The number is not 0"
		return test_pb2.output(status=answer)
		

