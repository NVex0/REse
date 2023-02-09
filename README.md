**Forensic** là tính từ có nghĩa là, pháp y, liên quan đến các phương pháp khoa học để giải quyết tội phạm, liên quan đến việc kiểm tra các đồ vật hoặc chất có liên quan đến tội phạm.

Trong lĩnh vực an toàn thông tin, **Forensics** hay còn gọi là điều tra số là công việc phát hiện, bảo vệ và phân tích thông tin được lưu trữ, truyền tải hoặc được tạo ra bởi một máy tính hoặc mạng máy tính, nhằm đưa ra các suy luận hợp lý để tìm nguyên nhân, giải thích các hiện tượng trong quá trình điều tra.

Trong CTF, Forensics gồm các dạng bài chính về:
- *Memory Forensics.*
- *File Forensics.*
- *Network Forensics.*
- *Image Forensics.*


**Image Forensics:**
- Tìm kiếm dữ liệu ẩn được giấu trong file ảnh, bằng nhiều kĩ thuật giấu tin `(Steganography)` khác nhau.
	Ví dụ như:
- giấu tin bằng Least Significant Bit (LSB) : các LSB khi bị thay đổi giá trị sẽ không gây ra thay đổi đáng kể, từ đó 1 file ảnh khi nhìn bằng mắt thường không thể thấy được sự thay đổi sau khi đã giấu tin mật vào ảnh đó.
- giấu tin vào 1 kênh màu khác của ảnh: tức tin mật vô hình trên 1 kênh màu này nhưng lại hiện ra trên 1 kênh màu khác:
    
				Tool:
					- Stegsolve.
					- Tự viết code dùng thư viện PIL, OpenCV trên python.
- giấu trong data của file ảnh:
    
				Tool:
					- Strings, thường dùng cùng Grep.
					- Binwalk.	
					- Exiftool. 
					- Zsteg. (PNG, BMP).
					- Steghide. (JPEG, BMP).
					- Stegcracker.
- cũng cùng category Stegano, ngoài Image còn có cả giấu tin trong các file âm thanh:

                      Tool:
					- Sonic Visualizer.
					- Wavesteg.
          
**Memory Forensics:**
  
* Điều tra bộ nhớ RAM được ghi lại tại thời điểm có dấu hiệu nghi ngờ hoặc bị tấn công.
* Để ghi lại bộ nhớ RAM tại thời điểm đó, có các tool như:

			- DumpIt.
			- FTK Imager.
      
* Với các bài memory forensics, phải xác định được các thông tin cơ bản của memory image đó. Quan trọng là xác định được OS của nó. 

				Tool:
					- Volatility.
* PID: ID của tiến trình, mỗi tiến trình có 1 PID riêng biệt.
* PPID: ID của tiến trình cha của 1 tiến trình con.
* Các plugins cơ bản của Volatility:

				- imageinfo: xác định thông tin cơ bản của memory image.
				- pslist : lấy thông tin các tiến trình. Tuy nhiên nó không liệt kê được các tiến trình ẩn hoặc bị kết thúc.
				- psscan : giải quyết được vấn đề trên.
				- pstree : hiển thị thông tin các tiến trình dưới dạng cây -> dễ nhìn, cha nào con đó.

**Disk Forensics:**

*  Thu thập, phân tích dữ liệu được lưu trữ trên phương tiện lưu trữ vật lý, nhằm trích xuất dữ liệu ẩn, khôi phục các tập tin bị xóa, qua đó xác định người đã tạo ra những thay đổi dữ liệu trên thiết bị được phân tích.
* 1 số challenge của Disk Forensics như:
	- Khôi phục File.
	- Phân tích File đáng ngờ thu được.
	
                          Tool:
					- Encase: Thu thập dữ liệu từ nhiều nguồn thiết bị, phân tích ổ đĩa 1 cách toàn diện.
					- Sleuthkit: phân tích ảnh ổ đĩa và khôi phục file từ nó.
					- FTK: quét ổ đĩa để mình vào tìm thông tin.
        
**Network Forensics:**
- Thu thập và phân tích các gói tin được truyền qua các thiết bị đầu cuối, từ đó phát hiện, cảnh báo các dấu hiệu bất thường trong hệ thống mạng.

				Tool:
					- Wireshark : bắt và phân tích gói tin với giao diện đồ họa.
					- tcpdump : bắt và phân tích gói tin với giao diện console.
					- Tshark: command line tool của Wireshark.
					- netcat : debug kết nối, đóng vai trò cả client và server, console trên windows và linux.
					- nmap : quét cổng.
					- Snort : phát hiện xâm nhập mạng.
					- nslookup.
          
- Các bài dạng này sẽ làm việc với file PCAP - là dump file ghi lại traffic thời điểm nạn nhân bị tấn công hoặc có dấu hiệu đáng ngờ.

**File Forensics:**
- Đại khái là phân tích đủ các loại file (.-.) ?
- File Signature:

				Dùng để xác minh được loại tệp, ví dụ file PNG sẽ có signature là (89 50 4E 47 0D 0A 1A 0A)
								      file JPG thì là (FF D8 FF E0)
								           PDF (25 50 44 46 2D)
								           7z archive (37 7A BC AF 27 1C) etc...
                           
- Các dạng thường gặp sẽ là:

	* Tìm file này ẩn trong file kia.
  
			Tool:
					- binwalk.
          
	* Sai extension.
  
		- Check bằng command (file) rồi sửa lại.
		- Dùng 1 trình hex editor để xem signature rồi sửa lại.
    ```
        Tool:
			- HxD.
                    - Bless.
    ``` 
	* Sai header.
  
				- Dùng trình hex editor như trên.
				- PNGcheck. (check PNG có bị corrupt hay không.)
        
	* File cần pass để mở. Ví dụ các file nén.
  
				Tool:
					- Fcrackzip.
					- JohntheRipper.
