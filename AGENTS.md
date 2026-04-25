# Dự báo phụ tải điện ngắn hạn 
Repo chứa các tài liệu liên quan đến đồ án tốt nghiệp với mục tiêu ứng dụng Al cho việc dự báo phụ tải điện ngắn hạn. 
. Sinh viên: Nguyễn Anh Dũng - MSSV: 20222497

## Cấu trúc thư mục

```
SHORT_TERM_ELECTRICITY_LOAD_FORECASTING/
├── ai_docs/
│   └── thesis_split/
│       ├── ch01_introduction.md              # Bài toán, mục tiêu, phạm vi nghiên cứu
│       │   
│       ├── ch02_load_forecasting_overview.md
│       │   # Tổng quan dự báo phụ tải điện, các yếu tố ảnh hưởng, các hướng tiếp cận
│       ├── ch03_01_feedforward_nn.md
│       │   # CSLT mạng nơ-ron truyền thẳng (FNN)
│       ├── ch03_02_elm.md
│       │   # CSLT Extreme Learning Machine (ELM)
│       ├── ch03_03_pso.md
│       │   # CSLT Particle Swarm Optimization (PSO)
│       ├── ch03_04_metrics.md
│       │   # Metrics: MAE, MAPE, RMSE
│       ├── ch04_01_data_description.md
│       │   # Mô tả dataset
│       ├── ch04_02_data_preprocessing.md
│       │   # Tiền xử lý dữ liệu: làm sạch, xử lý thiếu, chuẩn hóa
│       ├── ch04_03_data_analysis.md
│       │   # Phân tích dữ liệu khám phá (EDA), tương quan, phân phối
│       ├── ch04_04_input_feature_selection.md
│       │   # Chọn đặc trưng đầu vào cho mô hình
│       ├── ch04_05_hybrid_elm_pso_design.md
│       │   # Thiết kế mô hình lai ELM-PSO
│       ├── ch04_06_workflow.md
│       │   # Quy trình chạy chương trình: load data → train → test → đánh giá
│       ├── ch05_01_test_performance.md
│       │   # Kết quả dự báo trên tập test
│       ├── ch05_02_convergence.md
│       │   # Phân tích hội tụ của PSO
│       ├── ch05_03_comparison.md
│       │   # So sánh ELM thường và PSO-ELM
│       ├── ch05_04_discussion.md
│       │   # Thảo luận kết quả thực nghiệm
│       └── ch06_conclusion_future_work.md
│           # Kết luận, hạn chế, hướng phát triển tiếp theo
│
├── docs/
│   ├── decision/         # Ghi chú quyết định đến thiết kế
│   │   
│   ├── architecture.md   # Kiến trúc sơ đồ khối từ tổng thể đến chi tiết
│   │   
│   ├── design.md         # Khung code và flow code
│   │   
│   ├── requirement.md    # Yêu cầu bài toán (yêu cầu kỹ thuật)
│   │   
│   └── use_case.md       # Các use case nghiệp vụ hoặc kịch bản sử dụng (kịch bản thử nghiệm)
│       
│
├── scripts/              # 
│   
│
├── src/
│   ├── data/
│   │   ├── energy.csv    # Dữ liệu năng lượng / phụ tải / giá điện
│   │   │   
│   │   └── weather.csv   # Dữ liệu thời tiết
│   │       
│   │
│   └── model/
│       ├── model_v1.py   # Baseline ELM
│       │   
│       ├── model_v2.py   # ELM-PSO
│       │   
│       ├── clean_data.py # Làm sạch dữ liệu, xử lý thiếu, ngoại lai, chuẩn hóa (sau merge_data.py)
│       │   
│       ├── merge_data.py # Ghép dữ liệu energy và weather, tạo tập dữ liệu huấn luyện
│       │   
│       ├── test.py       # Chạy đánh giá mô hình trên tập test
│       │   
│       ├── train.py      # Huấn luyện mô hình
│       │   
│       └── visualize_data.py  # Vẽ biểu đồ EDA, dự báo, hội tụ, so sánh kết quả
│           
│
├── tests/                 # Unit test / integration test cho code
│  
│
└── CLAUDE.md              # File hướng dẫn/quy ước làm việc cho AI assistant hoặc contributor
    
```

## Coding convention



## Build



## ... Source


## Tài liệu tham khảo


## Ngôn ngữ