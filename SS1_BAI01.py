# lỗi chương trình là do kỹ sư phần mềm truyền vào dòng print('Tên bệnh nhân') là dữ liệu nhập vào của "Triệu chứng", các trường khác hiển thị sai là do in ra màn hình thông tin không khớp với biến lưu trữ thông tin
#Mã nguồn chuẩn:
print('--hệ thống tiếp nhận bệnh nhân --')
name_patient = input("Nhập tên bệnh nhân: ")
age= int(input("nhập tuổi bệnh nhân:"))
symtom=input("Mời bạn nhập triệu chứng: ")
print('------Phiếu khám bệnh-------')
print ('Tên bệnh nhân: ', name_patient)
print("Tuổi: ", age)
print("Triệu chứng: ",symtom)