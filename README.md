# Hệ Thống Lưu Trữ Dữ Liệu Dựa Trên Blockchain

Dự án này là một hệ thống dựa trên blockchain, cho phép lưu trữ, truy xuất và giao tiếp dữ liệu an toàn giữa các thực thể. Hệ thống sử dụng các hợp đồng thông minh được triển khai trên blockchain Ethereum, IPFS để lưu trữ phi tập trung, và các kỹ thuật mật mã để đảm bảo tính toàn vẹn và bảo mật của dữ liệu.

## Mục Lục

1. [Tổng Quan](#tổng-quan)
2. [Tính Năng](#tính-năng)
3. [Cài Đặt](#cài-đặt)
4. [Cách Sử Dụng](#cách-sử-dụng)


## Tổng Quan

Hệ thống này cho phép người dùng lưu trữ và truy xuất dữ liệu một cách an toàn bằng cách kết hợp blockchain và IPFS. Dữ liệu được mã hóa và có thể được xác thực bằng chữ ký số. 

## Tính Năng

- **Hợp Đồng Thông Minh:** Hợp đồng thông minh dựa trên Solidity được triển khai trên blockchain Ethereum để xử lý việc lưu trữ, truy xuất dữ liệu và nhắn tin.
- **Tích Hợp IPFS:** Lưu trữ phi tập trung dữ liệu bằng IPFS, đảm bảo rằng dữ liệu không chỉ an toàn mà còn chống lại việc sửa đổi.
- **Bảo Mật Mật Mã:** Dữ liệu được mã hóa bằng AES và chữ ký được xác thực bằng RSA, đảm bảo tính toàn vẹn và tính xác thực của dữ liệu.

## Cài Đặt

Để thiết lập hệ thống, bạn cần cài đặt các phần mềm sau:

- [Node.js](https://nodejs.org/)
- [Ganache CLI](https://www.trufflesuite.com/ganache)
- [Python 3.x](https://www.python.org/)
- Các thư viện Python cần thiết:
- **web3**: Thư viện để tương tác với blockchain Ethereum.
- **ipfshttpclient**: Thư viện để tương tác với IPFS (InterPlanetary File System).
- **cryptography**: Thư viện để thực hiện các hoạt động mã hóa, bao gồm AES và RSA.
- **solcx**: Thư viện để biên dịch và triển khai hợp đồng thông minh Solidity từ Python.

### Cài Đặt Các Thư Viện
Bạn có thể cài đặt tất cả các thư viện cần thiết bằng lệnh sau:

```bash
pip install web3 ipfshttpclient cryptography solcx
```

```bash
npm install -g ganache-cli

### Hướng dẫn cài đặt
1. Download file go-ipfs trên repo, giải nén và gán địa chỉ vào Path của User ở mục Environment Variables
2. Khởi chạy ganache-cli và ipfs daemon trong Terminal bằng các lệnh sau

```bash
ganache-cli
```

```bash
ipfs init
```

```bash
ipfs daemon
```
Truy cập thư mục và mở terminal, chạy chương trình với lệnh `py test2.py`
## Cách sử dụng
![fe124f62-7ecf-4823-8f69-386d07d95ee6](https://github.com/user-attachments/assets/f7c289b1-5f58-430d-b03e-437e54ba12cf)
Trang chủ chương trình
![f4ba470e-2ede-434c-94f0-20a0e02c687c](https://github.com/user-attachments/assets/645b5f60-a177-4547-8a74-2883986a67ed)
Lựa chọn vai trò ( Bác sĩ, bệnh nhân, cửa hàng thuốc,...)
![44250f9c-d242-4fd2-8e4d-3b3672efa702](https://github.com/user-attachments/assets/fc1f74ea-81b5-4fba-940d-2ae0870d71e6)
Đăng nhập với thông tin của mình 
![692868da-9dc1-4e88-9595-29fa9bb7165c](https://github.com/user-attachments/assets/be736342-0c20-45ed-8000-74f71156d379)
Chương trình cho phép nhiều lựa chọn bao gồm upload và kiểm tra chữ kí



