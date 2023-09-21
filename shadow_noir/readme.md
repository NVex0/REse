Khi xem ảnh trên từng kênh, để ý hình rõ mà ta thấy chỉ kênh alpha mới có:

![image](https://github.com/NVex0/REse/assets/113530029/13c9983f-c482-491f-898c-b26a3fbdd6a2)

Ta bỏ kênh alpha ra và còn lại 3 kênh RGB:

![image](https://github.com/NVex0/REse/assets/113530029/180333b9-ba90-416d-a52c-be6a4fccd84c)

Nhìn các vân màu khá đều trên ảnh, nếu tiếp xúc đủ nhiều các bài thế này, ta có thể đoán đây có thể là biểu diễn của kiểu dữ liệu thô. Tức là bức ảnh này hoàn toàn có thể là biểu diễn dữ liệu thô của 1 video.

Loại file nào mà vừa được biểu diễn dưới dạng video lẫn dạng ảnh được? -> ta có thể nghĩ ngay tới webm. Mình sẽ thực hiện convert nó qua webm:

![image](https://github.com/NVex0/REse/assets/113530029/a6384503-b9a2-4e82-a058-16ece0dbd56f)

> Ta đã bỏ kênh alpha đi, từ đó pix_fmt sẽ chỉ còn 3 kênh, và từ đó ta chọn plugin rgb24.

> Như đã đề cập, ta đang xử lý nó dưới dạng dữ liệu thô của video, và đó là plugin cho phần -f.

Mình được 1 video webm như này:

https://github.com/NVex0/REse/blob/main/shadow_noir/out.webm

để ý tiêu đề vid là `QmluYXJ5IExpZ2h0`, mình decode thử thì có được nội dung sau:

![image](https://github.com/NVex0/REse/assets/113530029/bc927359-30c0-4651-b457-0385422e7510)

Đây có thể là hint cho chúng ta cho bước tiếp theo, khi theo dõi video, ta để ý có cột sáng nhấp nháy liên tục, từ đó mình có ý tưởng từ hint `Binary Light` là sẽ extract tín hiệu nhấp nháy đó ra dạng binary để decode.

Mình dùng ffmpeg để tách ra các frame, mình chọn BMP vì loại ảnh này không sử dụng thuật toán nén, từ đó khi làm việc với màu trên ảnh sẽ chính xác hơn, vì nó nguyên tác mà :v 

![image](https://github.com/NVex0/REse/assets/113530029/f3846182-5ef2-41eb-903a-8b3053122a9a)

Và viết 1 quick script, ta sẽ lấy màu vàng và màu trắng của đèn ra dưới dạng binary:

![image](https://github.com/NVex0/REse/assets/113530029/4a9e5ac5-4b0b-486f-9d06-edb9d088f897)

Có thể thấy được 1 dãy binary bị lặp lại mấy lần, mình sẽ chỉ lấy 1 lần của dãy đó ra decode thử:

![image](https://github.com/NVex0/REse/assets/113530029/22a407cd-2069-4223-86f6-634a6778ef30)

Và ta có được flag: `a_Pe4c3fuL_MoRn1ng`
