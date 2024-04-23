from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import tiktoken
tokenizer = AutoTokenizer.from_pretrained("VietAI/vit5-large-vietnews-summarization")  
model = AutoModelForSeq2SeqLM.from_pretrained("VietAI/vit5-large-vietnews-summarization")


sentence = """Điện ảnh đã và đang góp phần không nhỏ quảng bá danh lam thắng cảnh, giá trị văn hóa, di sản của các vùng miền đến với công chúng, giúp thu hút khách du lịch và thúc đẩy sự phát triển kinh tế-xã hội của địa phương. Thực tế cho thấy, nhiều địa điểm là bối cảnh trong tác phẩm điện ảnh đã trở thành địa chỉ thu hút đông đảo du khách tìm đến. Tiêu biểu thời gian qua có thể kể đến lượng khách ồ ạt đổ về “Nhà của Pao” ở xã Sủng Là, huyện Đồng Văn, tỉnh Hà Giang sau thành công của bộ phim “Chuyện của Pao”; hay việc gia tăng đột biến số lượng du khách đến với quần thể Di sản thế giới Tràng An (Ninh Bình) ngay khi phim “Kong Skull Island” ra mắt năm 2017. Tại các địa danh ít được biết đến như ngôi làng Đo Đo ở xã Bình Quế (Thăng Bình, Quảng Nam) cũng trở nên nổi tiếng, được nhiều người tìm đến trải nghiệm sau khi bộ phim “Mắt biếc” công chiếu. Mới đây, bối cảnh xuất hiện trong các bộ phim “Tết ở làng Địa Ngục”, “Kẻ ăn hồn” cũng được khán giả săn tìm và đến thăm, đó là làng Sảo Há, xã Vần Chải, huyện Đồng Văn, tỉnh Hà Giang.

Là quốc gia sở hữu nhiều cảnh quan thiên nhiên ấn tượng và bản sắc văn hóa độc đáo, đa dạng nhưng so với nhiều nước trong khu vực, Việt Nam chưa thật sự trở thành điểm đến hấp dẫn đối với các đoàn làm phim nước ngoài, thậm chí ngay chính các đoàn làm phim trong nước cũng vấp phải không ít rào cản. Tiềm năng du lịch của nhiều vùng chưa được các nhà làm phim “đánh thức” và khai thác một cách hiệu quả. Từ đây đặt ra vấn đề: Các địa phương đã sẵn sàng mời gọi, “trải thảm đỏ” đón các nhà làm phim trên tinh thần hợp tác đôi bên cùng có lợi? Không ít đoàn làm phim đi tìm bối cảnh tại các địa phương song gặp phải sự kém mặn mà của chính quyền địa phương cũng như cơ quan chức năng. Cùng với đó họ phải đối mặt với nhiều thủ tục phiền hà, chồng chéo và những quy định hành chính cứng nhắc, mất thời gian, làm gia tăng đáng kể chi phí, khiến dự án làm phim bị chậm tiến độ, đội vốn.
"""
text =  "vietnews: " + sentence + " </s>"
encoding = tiktoken.get_encoding("cl100k_base")
tokens = encoding.encode(text)
print(len(tokens))
encoding = tokenizer(text, return_tensors="pt")
input_ids, attention_masks = encoding["input_ids"], encoding["attention_mask"]
outputs = model.generate(
    input_ids=input_ids, attention_mask=attention_masks,
    max_length=256,
    early_stopping=False
)
for output in outputs:
    line = tokenizer.decode(output, skip_special_tokens=True, clean_up_tokenization_spaces=True)
    print(line)
