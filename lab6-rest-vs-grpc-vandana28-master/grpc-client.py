import grpc

# import the generated classes
import sum_pb2
import sum_pb2_grpc
import struct
import sys
from time import perf_counter

endpoint = sys.argv[1]
num_iterations = sys.argv[2]
n = int(num_iterations)
img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

#### ADD
if(endpoint == 'add'):
    stub = sum_pb2_grpc.addStub(channel)
    count = 1
    t1_start = perf_counter()
    while(count <=n):
        number = sum_pb2.addMsg(a=5,b=10)
        response = stub.add(number)
        print(response.a)
        count = count+1
    t1_stop = perf_counter()
    total_time = t1_stop - t1_start
    time_per_query = total_time/n
    print(time_per_query)

else:

    stub = sum_pb2_grpc.imageStub(channel)
    count = 1
    t1_start = perf_counter()
    while(count <=n):
        number = sum_pb2.imageMsg(img=img)
        response = stub.image(number)
        print(response.a,response.b)
        count = count+1
    t1_stop = perf_counter()
    total_time = t1_stop - t1_start
    time_per_query = total_time/n
    print(time_per_query)
#print(response.img)
#y= int.from_bytes(response.img,byteorder="big")


# # 
# # testResult=struct.unpack('b', response.img)
# x=sys.getsizeof(response.img)
# y= int.from_bytes(response.img,byteorder="big")
# print(y)