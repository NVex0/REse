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

* Ví dụ: `hashcat -a 0 -m 14600 hackers-drive.dd rock.txt`

> * Ex: Tấn công file `hackers-drive.dd` kiểu Dictonary, cho thuật toán LUKS v1 (legacy) 10. Sử dụng wordlist tự tạo `rock.txt`.

# III. Pkcrack & Bkcrack.
* Đây là 2 tool tấn công / bẻ khoá archive dựa trên phương thức: tấn công bản rõ đã biết (KPA). 
> + Sơ lược về KPA: là tấn công khi attacker có cả bản rõ lẫn bản mã tương ứng của nó. Rồi từ đó phân tích, đoán ra cách thức mã hoá hay khoá bí mật của nó, hoặc tự phát triển cho mình 1 thuật toán cho phép mình giải bất kì bản mã nào khác.

## Pkcrack: 
+ Pkcrack yêu cầu phải có 2 file zip: 1 zip là zip cần để crack, 1 zip chứa ÍT NHẤT 1 file từ bên zip cần crack kia, và bản rõ đó phải ở dạng `unencrypted`. Và 2 file zip này phải có cùng cách compress.
+ Sử dụng: Lệnh thông thường của Pkcrack là:

 `./pkcrack -C encrypted-ZIP -c ciphertextname -P plaintext-ZIP 
          -p plaintextname -d decrypted_file -a`
         
> + Với -C là file zip cần crack. 
> + -P là file zip chứa bản rõ.
> + -c và -p là các entry tương ứng với zip đó. 
> + -d xác định file sẽ lưu trữ data của encrypted zip sau khi crack. Nếu trong lệnh không có `-d` thì sau khi tìm được bộ khoá là nó tự đi tìm mật khẩu của pkzip đó. Nếu nó không tìm được mật khẩu thì dùng bộ khoá kia để mở zip với `zipdecrypt` của pkcrack. Lệnh như sau:
> + + ` ./zipdecrypt khoá0 khoá1 khoá2 encrypted_archive decrypted_archive`
> + -a không biết :( . `./pkcrack -h` for more info.
> Tuy nhiên có thể rút bớt -C và -P. Sử dụng `./extract <Zip_file> <Name_in_Zip>` của pkcrack để lấy được các entry dưới dạng đã compress ra.

Ví dụ như bài `Keep_Out.zip` của HCMUS:
+ Ở bước crack `dat2fish stash.zip`, dùng lệnh sau:

`./pkcrack -C ~/Desktop/dat2fish\ stash.zip -c bookmarks.txt -P ~/Desktop/bookmarks.zip -p bookmarks.txt -d out.zip -a` 
Sau khi crack thành công sẽ trả ra `out.zip` là file zip đã được crack.

## Bkcrack:
+ Tương tự như `Pkcrack`, nếu có 2 file zip đã đáp ứng yêu cầu thì chạy lệnh như sau:

`./bkcrack -C encrypted.zip -c cipher -P plain.zip -p plain -d decipheredfile`

+ Sau khi crack thành công. Bkcrack trả về cho ta 1 bộ khoá. Ta có thể lựa chọn khôi phục pass gốc, tạo pass mới, hoặc dùng luôn bộ khoá kia cho nhanh:
1. Khôi phục pass gốc:

`./bkcrack -k khoá0 khoá1 khoá2 -r <lenght> ?p` . ví dụ length của pass như là 9, 10, hay 11...13 gì đó. Hơi mất thời gian.

2. Tạo pass mới:

`./bkcrack -C encrypted.zip -k khoá0 khoá1 khoá2 -U unlocked.zip password`
> Sau lệnh này là tạo cái zip mới tên "Unlocked", khoá với cái pass mình set ở chỗ password bên trên.

3. Dùng bộ khoá sau crack:

`./bkcrack -c cipherfile -k khoá0 khoá1 khoá2 -d decipheredfile` , hoặc với zip thì thay `-C` vào `-c`.
>  `decipheredfile` được trả về có thể bị compress hoặc không tuỳ vào việc compression có được sử dụng hay không (E không hiểu lắm). Dùng tool sau của bkcrack để decompress nó:
`python3 tools/inflate.py < decipheredfile > decompressedfile`

Ví dụ: 

Cũng bài `Keep_Out.zip` của HCMUS, đầu tiên tìm khoá:

- `./pkcrack -C ~/Desktop/dat2fish\ stash.zip -c bookmarks.txt -P ~/Desktop/bookmarks.zip -p bookmarks.txt`

- Crack thành công, lấy được bộ khoá: `99075ea6 102ed4f6 fcaa1b2b`

- Nhồi bộ khoá vào để mở zip:

`./bkcrack -C ~/Desktop/dat2fish\ stash.zip -k 99075ea6 102ed4f6 fcaa1b2b -d out.zip`

Done.

 --- 
 ---
## Điểm giống: 
2 tool cũng na ná nhau, ngoài các option riêng của nó thì vẫn chung đặc điểm là -C -c -P -p cho 1 lần crack thông thường.

## Điểm khác: 
1. Bkcrack xem được entries. (Mặc dù hơi vô dụng vì mở thử zip lên là thấy rồi :v)
2. Bkcrack không có extract file ra dưới dạng compress. (Hoặc e chưa tìm ra).
3. Tuy nhiên bù đắp vào cái thứ 2 thì Bkcrack có thể chỉ cần dùng `-c` và `-p`:

`./bkcrack -c cipherfile -p plainfile`
+  Với 2 đầu vào này là bản rõ và bản mã tương ứng với nhau. Nếu bản rõ tương ứng với phần khác thay vì tương ứng với phần đầu của bản mã thì nhét thêm `-o` vào để tuỳ chỉnh offset:
  
`./bkcrack -c cipherfile -p plainfile -o offset`


