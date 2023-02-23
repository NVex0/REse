# I. JohnTheRipper(JtR).
* 1 tool dùng để crack hash. `JohnTheRipper` được tích hợp sẵn khả năng tự nhận diện thuật toán hash, nên ta không cần phải xác định thuật toán hash rồi mới crack giống như `hashcat` (Mục II).
* Để xem các thuật toán mà `JohnTheRipper` hỗ trợ, có thể dùng lệnh sau:  `john --list=formats`
* JtR có các mode như sau được xài nhiều nhất:  
### 1. Single crack mode. 
+ John sẽ nhận vào 1 string ta cho trước, rồi generate hàng loạt biến thể dựa trên cái string đấy.
> + Ví dụ: file text `formathash.txt` chứa string và hash : `stealth:d776dd32d662b8efbdf853837269bd725203c579`
> 
> + Thêm  `--single` để set JtR vào Single crack mode, dùng lệnh sau: `john --single --format=raw-sha1 formathash.txt`.
> 
> + Lấy được pass là `StEaLtH`.
### 2. Dictionary mode.
+ John sẽ nhận vào 1 wordlist ta cho trước, sau đó nó sẽ tạo hash của từng từ trong wordlist đó rồi so sánh với hash cần crack. Nếu ra giống nhau thì crack thành công.
> + Thêm `--wordlist=<PATH>` để cung cấp wordlist cho JtR. JtR có 1 wordlist riêng của nó ở path `/usr/share/wordlists/john.lst`. List này có vẻ chú bé đần hơn `/usr/share/wordlists/rockyou.txt`. Nhưng mà dùng cái nào cũng được, hiệu quả là được.

### 3. Incremental mode.
+ Mode ác nhất của JtR, nó sẽ thử tất cả các kết hợp kí tự để tạo pass với pass có độ dài set trước.
> + Dùng lệnh như sau: `john -i:<digits> passwordfile.txt`. Với `-i` để vào Incremental mode, và digits là độ dài tối đa của pass mà mình set.

### * 1 số ví dụ:

+ Dùng John để crack pass người dùng linux:
> Mật khẩu người dùng được lưu trữ dưới dạng hash sẵn trong directory `/etc/shadow` . Để crack, sử dụng lệnh `john /etc/shadow`.

+ Dùng John để crack tệp Zip/Rar có pass:
> Vì John là công cụ crack hash, trước tiên phải chuyển tệp sang lưu trữ hash bằng `zip2john` (đối với Zip) và bằng `rar2john` (đối với Rar). Lệnh như sau: `zip2john test.zip > hash.txt`. File `hash.txt` sẽ chứa giá trị hash trong đó.
> Tiếp theo là crack, với lệnh `john hash.txt`. Hoặc muốn nó chạy nhanh hơn thì xác định và thêm format cho nó. Ví dụ: `john --format=zip hash.txt`.


# II. Hashcat.
* Tool crack hash / password recovery từ hash nhanh nhất hiện giờ trên CLI. Hashcat cung cấp cho người sử dụng 4 chế độ tấn công/khôi phục mật khẩu khác nhau áp dụng cho hơn 300 thuật toán hash khác nhau. Tuy nhiên như đã đề cập ở mục I, `hashcat` không nhận diện được thuật toán hash, thế nên ta cần xác định thuật toán hash rồi mới crack được.

* 1 câu lệnh hashcat để tấn công có cú pháp cơ bản như này: 
> * `hashcat -a <cách tấn công> -m <thuật toán hash> <file chứa hash đầu vào> <wordlist>`.
> * Với `-a` là số của cách tấn công:
> * * `-a 0` : `Dictionary`.
> * * `-a 1` : `Combination`. Giống `Dictionary` nhưng cần 2 wordlist, hợp với việc mò cả user lẫn password. 
> * * `-a 3` : `Mask`. Chơi với loạt tổ hợp từ các kí tự được cho trước. (Ví dụ a,b,c thì cho ra tổ hợp abc, acb các thứ).
> * * `-a 6` và `-a 7` : `Hybrid`. Kết hợp cả `Dictionary` và `Mask`.
> * `-m` là số của thuật toán hash. Dùng `hashcat -help` để xem và chọn. Ví dụ `-m 0` là cho MD5 hash.

# III. Pkcrack.
# IV. Bkcrack.
