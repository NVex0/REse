## Cấu trúc hợp lệ cơ bản của 1 file ảnh PNG như sau:

* File signature: 

    hex: `89 50 4E 47 0D 0A 1A 0A` - Nó sẽ xác định được định danh cho file này là 1 file PNG, với:
    
    + byte đầu : `89` - nhằm giảm khả năng text file bị nhận diện thành PNG. (vì nó là non ASCII)
    
    + 3 bytes kế : `50 4E 47` là tên định dạng của file. (dạng ASCII là 'PNG')
    
    + 2 bytes tiếp theo : `0D 0A` là Carriage return - Line feed (CR-LF) giúp nhận diện lỗi truyền kém làm thay đổi trình tự dòng.
    
    + byte tiếp : `1A` - ngưng hiển thị tệp trong MSDOS.
    
    + byte cuối cùng : `0A` để kiểm tra quá trình dịch CR-LF có bị đảo ngược hay không.
   
* 1 Chunk IHDR:

    + Là chunk đầu tiên của 1 ảnh PNG, đi trước chunk IHDR là 4 bytes thể hiện size của IHDR (không tính 4 bytes đó).
    
    + Bắt đầu chunk IHDR là tên của nó : `49 48 44 52`
    
    + 4 bytes tiếp theo : thể hiện chiều rộng của ảnh. (pixel)
    
    + 4 bytes tiếp theo : thể hiện chiều dài của ảnh. (pixel)
    
    + byte tiếp : thể hiện độ sâu màu của ảnh. (bit-depth)
    
    + byte tiếp : thể hiện dạng màu của ảnh.
    
    + byte tiếp : thể hiện phương pháp nén.
    
    + byte tiếp : thể hiện phương pháp lọc.
    
    + byte cuối : thể hiện phương pháp đan xen.
    
* Chunk PLTE: 

    + Có thể có hoặc không có, optional. Nếu dạng màu bằng 3 thì bắt buộc phải có, dạng (2, 6) có thể có hoặc không, và dạng (0, 4) không được xuất hiện nó.
    
    + Chunk này phải xuất hiện trước chunk IDAT đầu tiên.
    
* 1 hay nhiều chunk IDAT:
    + Chứa data thực sự của ảnh.
    + Vì 1 ảnh PNG có thể chứa 1 hay nhiều chunk IDAT, thế nên các chunk IDAT phải liên tục mà không bị chunk khác gián đoạn.
    
    + Chunk IDAT dù chỉ có 1 byte hay chẳng có gì thì vẫn tính là hợp lệ, mặc dù nó thừa thãi.
    
* 1 Chunk IEND:

    + Chunk cuối cùng của PNG, đánh dấu sự kết thúc của dòng dữ liệu trong PNG.
    
    + Bắt đầu và kết thúc của chunk này là `49 45 4E 44 AE 42 60 82` , trường của chunk này được bỏ trống.


#### Mỗi Chunk cấu tạo từ 4 thành phần:
    
   + Độ dài chunk: là 1 số nguyên 4 bytes không dấu, thể hiện độ dài (tính theo byte) data của chunk đó.
   
   + Loại chunk: là một đoạn code dạng chunk 4 bytes.
   
   + Chunk data : dữ liệu của chunk đó.
   
   + CRC - Cyclic Redundancy Check: 4 bytes CRC được tính dựa trên những bytes trong chunk data và chunk type (loại chunk). Giá trị của CRC luôn hiển thị dù chunk có chứa data hay không.
