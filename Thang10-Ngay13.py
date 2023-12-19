
from queue import *
import math
'''
#Buôn dưa lê
if __name__ == '__main__':
    Q = queue.Queue()
    n, k, m = map(int, input().split())
    res = 0
    A = list(map(int, input().split())) + [0] * (k - 1)
    for i, x in enumerate(A, 1):
        Q.put([i, x])
        while i - Q.queue[0][0] >= k: Q.get()
        t = 0
        while Q.qsize() and t + Q.queue[0][1] <= m:
            t += Q.queue[0][1]
            Q.get()
        if Q.qsize():
            Q.queue[0][1] -= m - t
            t = m
        res += t
    print(res)  

#Buôn dưa lê
if __name__ == '__main__':
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = a + [0] * (k - 1)
    Q = Queue()
    res = 0
    for x in a:
        Q.put(x)
        while Q.qsize() > k: Q.get()
        t = 0
        while Q.qsize() and t + Q.queue[0] <= m: t += Q.get()
        if Q.qsize():
            Q.queue[0] -= m - t
            t = m
        res += t
    print(res)
    

# Liệt kê những số đi được trong bài mọi con đường về không
def bfs(n):
    Q = Queue()
    d = [0] * (n + 5)
    Q.put(n)
    d[n] = 1
    while Q.qsize():
        u = Q.get()
        for i in range(1, int(math.sqrt(u) + 1)):
            if u % i == 0:
                v = (i - 1)*(u // i+1)
                if d[v] == 0:
                    Q.put(v)
                    d[v] = 1
    for i in range(n + 1):
        if d[i] == 1: print(i, end = " ")
if __name__ == '__main__':
    bfs(int(input()))


# Robot: https://www.laptrinhonline.club/problem/tichpxrobot
def Sol(x, y):
    Q = Queue()
    Q.put((x, y))
    d = 1
    M = {(x, y): 1}
    while (Q.qsize()):
        x1, y1 = Q.get()
        if x1 % 2 == 0:
            if (y1, x1 / 2) not in M.keys():
                M[(y1, x1 / 2)] = 1
                Q.put((y1, x1 / 2))
                d += 1
        if y1 % 2 == 1:
            if ((y1 + 1) / 2, x1) not in M.keys():
                M[((y1 + 1) / 2, x1)] = 1
                Q.put(((y1 + 1) / 2, x1))
                d += 1
    print(d)



if __name__ == '__main__':
    x, y = map(int, input().split())
    Sol(x, y)
'''
    
def grade_school_multiplication(x, y):
  """Multiplies two numbers using the grade school algorithm.

  Args:
    x: The first number.
    y: The second number.

  Returns:
    The product of x and y.
  """

  product = 0
  for i in range(len(str(y))):
    power = 10**(len(str(y)) - i - 1)
    product += (int(str(y)[i]) * x * power)

  return product


# Example usage:

print(grade_school_multiplication(1234, 5678))
# Output: 7066332

'''

Quản lý phòng trọ

# Cách 1
    Đăng kí phòng trọ
        Tiếp nhận thông tin 
            Tiếp nhận nhu cầu về phòng
            Nhận thông tin cá nhân
            Đối chiếu nhu cầu với phòng đang trống

        Lưu thông tin khách (kể cả không thuê cũng lưu lại thông tin liên hệ, sau có thể cần)

    Xây dựng hợp đồng
        Tạo hợp đồng theo mẫu
        Kí kết
        Thu tiền cọc 
        Lưu lại hóa đơn

    Xử lý khi kí kết thành công
        Bàn giao nội thất phòng
        Thêm khách vào kênh liên lạc chung
        Khai báo tạm trú cho khách

    Xử lý định kì
        Thu tiền trọ
            Thu tiền phòng hàng tháng
            Lưu lại hóa đơn

        Kiểm tra cơ sở vật chất
            Kiểm tra hệ thống an ninh
            Kiểm tra hệ thống phòng cháy
            Kiểm tra nội thất 

        Bảo dưỡng hoặc thay thế
        Cập nhật tình trạng mỗi phòng trọ
            Xóa phòng 
            Thêm phòng
            Sửa các tiêu chí của phòng

    Kết thúc hợp đồng
        Xử lý khi khách hủy hợp đồng trước thời hạn
        Xử lý khi kết thúc hợp đồng đúng hạn
            Bàn giao lại nội thất phòng
            Trả lại tiền cọc 

    Truy xuất dữ liệu
        Xuất ra tổng doanh thu của tháng bất kì
        Hiển thị thông tin khách theo tên
        Lọc danh sách phòng theo các tiêu chí 

    

# Cách 2
    Quản lý khách hàng
        Xử lý đầu vào
            Tiếp nhận nhu cầu về phòng
            Nhận thông tin cá nhân
            Đối chiếu với phòng trống
            Lưu thông tin khách

   
        Thêm khách vào kênh liên lạc chung
        Khai báo tạm trú cho khách
        

    Quản lý hợp đồng
        Xây dựng hợp đồng
        Kí kết
        
        Lưu trữ thông tin hợp đồng 

                
                

    Quản lý cơ sở vật chất
        Bảo trì cơ sở vật chất
            Kiểm tra cơ sở vật chất
                Kiểm tra hệ thống an ninh
                Kiểm tra hệ thống phòng cháy
                Kiểm tra nội thất 
        
            Bảo dưỡng hoặc thay thế     

        Cập nhật trạng thái phòng 
        Bàn giao nội thất phòng
            Bàn giao khi thuê
            Bàn giao khi trả

    Quản lý thu chi 
        Thu tiền 
            Thu tiền thuê phòng hàng tháng
            Thu tiền cọc 
            Lưu lại hóa đơn 
        
        Chi
            Trả tiền bảo trì
            Trả lại tiền cọc

        

    Thống kê dữ liệu
        Báo cáo thu, chi hàng tháng
        Tìm kiếm thông tin khách

        

            
'''