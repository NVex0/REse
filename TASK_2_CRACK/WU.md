## I. Sử dụng JohnTheRipper crack Keep_Out.zip.

`zip2john Keep_Out.zip > hash`

`john --wordlist==/usr/share/wordlists/rockyou.txt/hash`

=> Pass : `MANCHESTERUNITED`

## II. Crack dat2fish stash.zip.

Ta biết được 1 file strong stash, Encryption Method của zip là `ZipCrypto` => Known Plaintext Attack.

#### Cách 1: Pkcrack.

* Bước 1: Zip lại file `bookmarks.txt` với: Compression Level 5 - Normal || Compression Method - Deflate || Encryption Method - ZipCrypto (Cùng kiểu với `dat2fish stash.zip`)
* Bước 2: `./pkcrack -C ~/Desktop/dat2fish\ stash.zip -c bookmarks.txt -P ~/Desktop/bookmarks.zip -p bookmarks.txt -d out.zip -a`
* Bước 3: Unzip `out.zip`. Mở file `confidential.pdf`. Thấy text trong pdf bị redacted, bôi đen lên là thấy flag.

#### Cách 2: Bkcrack dùng file `bookmarks.txt`.

* Bước 1: Giống Bước 1 Pkcrack.
* Bước 2: `./bkcrack -C ~/Desktop/dat2fish\ stash.zip -c bookmarks.txt -P ~/Desktop/bookmarks.zip -p bookmarks.txt` => Lấy được keys: `99075ea6 102ed4f6 fcaa1b2b`
* Bước 3: Set pass mới: `1234` cho zip `./bkcrack -C ~/Desktop/dat2fish\ stash.zip -k 99075ea6 102ed4f6 fcaa1b2b -U out.zip 1234`
* Bước 4: giống Bước 3 Pkcrack, Unzip dùng pass mới set ở Bước 3.

#### Cách 3: Bkcrack không dùng file `bookmarks.txt`.

Solutions: khi không có bookmarks.txt. Xem các entry khác bằng lệnh `./bkcrack -L ~/Desktop/dat2fish\ stash.zip`.\
- Bkcrack dựa trên phương thức tấn công bản rõ đã biết, và yêu cầu tối thiểu phải có 12 bytes bản rõ, với 8 bytes liên tục. Nhìn qua các entries của zip, 8 bytes liên tục khả thi chỉ có file png. 8 bytes liên tục của png có phần signature và IEND, tuy nhiên sig có non-ASCII nên e không cop được :(, v nên e sử dụng IEND làm 8 bytes đó. 
Để đệm thêm cho đủ thì lấy thêm mấy phần đầu của critical chunk vào:  

``echo -n 'PNGIHDRIDATIEND®B`‚' > plain.txt``
