### Codecamp #รุ่น3
  1. Waranya Thamsritip

  2.1. โหลด Dataset เข้าไปใน Python Pandas

  2.2. เขียนโค้ดแสดง หัว10แถว ท้าย10แถว และสุ่ม10แถว

  2.3. ใช้ info และ describe อธิบายข้อมูลเบื้องต้น

  2.4. ใช้ pairplot ดูความสัมพันธ์เบื้องต้น

  2.5. เช็คค่า Correlation ของ Dataset

  2.6.ใช้ Correlation ทำ Heatmap

  2.7. สร้าง scatter plot ของความสัมพันธ์ที่มี Correlation สูงสุด

  2.8. สร้าง scatter plot ของความสัมพันธ์ที่มี Correlation ต่ำสุด

  2.9. สร้าง scatter plot ของความสัมพันธ์ที่มี Correlation ใกล้ 0 ที่สุด

  2.10. ใช้ seaborn และ matplotlib สร้าง subplot 9 รูป (3x3) แต่ละรูปเป็น boxplot ของ Feature 1 – Feature 9

  2.11. ใช้ seaborn และ matplotlib สร้าง subplot 4 รูป (2x2) แต่ละรูปเป็น boxplot ของ Feature 10 – Feature 13

  2.12. จากข้อ 10-11 สามารถจัดการกับ Outliers ได้ตามความเหมาะสม

  2.13. เช็คว่ามีข้อมูลหายไปหรือไม่ สามารถจัดการได้ตามความเหมาะสม

  2.14. เพิ่มผลลัพธ์เป็นคอลัมน์ที่ 14

  2.15. Split ข้อมูลด้วย train_test_split โดยใช้อัตราส่วน 60:40

  2.16. ทำ Feature Scaling ด้วย Standardization โดยใช้ข้อมูล X_train เป็นตัว fit

  2.17. สร้างโมเดลแบบ Support Vector Machine (เป็น Baseline) 

  2.18. สร้าง countplot ของค่าที่ทำนายโดย Support Vector Machine

  2.19. วัดผลโมเดล SVM โดยใช้ confusion matrix

  2.20. ประเมินผลโมเดล SVM ด้วยคะแนน Accuracy, F1 score, Recall, Precision ทั้งแบบ Micro, Macro

  2.21. ทำ Hyperparameter tuning ด้วย GridSearchCV กับ SVM

  2.22. วัดผลโมเดล SVM หลัง Hyperparameter tuning ด้วย confusion matrix

  2.23. ประเมินผลโมเดล SVM หลัง Hyperparameter tuning ด้วยคะแนน Accuracy, F1 score, Recall, Precision ทั้งแบบ Micro, Macro

  2.24. สร้างโมเดลแบบ Random Forest (เป็น Baseline) 

  2.25. สร้าง countplot ของค่าที่ทำนายโดย Random Forest 

  2.26. วัดผลโมเดล Random Forest ด้วย confusion matrix 

  2.27. ประเมินผลโมเดล RF ด้วยคะแนน Accuracy, F1 score, Recall, Precision ทั้งแบบ Micro, Macro

  2.28. ทำ Hyperparameter tuning ด้วย GridSearchCV กับ RF 

  2.29. วัดผลโมเดล Random Forest หลัง Hyperparameter tuning ด้วย confusion matrix 

  2.30. ประเมินผลโมเดล RF หลัง Hyperparameter tuning ด้วยคะแนน Accuracy, F1 score, Recall, Precision ทั้งแบบ Micro, Macro

  2.31. ใช้ seaborn และ matplotlib สร้าง subplot 9 รูป (3x3) แต่ละรูปเป็น Distribution Plot ของ Feature 1 – Feature 9

  2.32. ใช้ seaborn และ matplotlib สร้าง subplot 4 รูป (2x2) แต่ละรูปเป็น Distribution Plot ของ Feature 10 – Feature 13

  2.33. จากข้อ 26-27 มีฟีเจอร์ใดบ้างที่เป็น Normal Distribution 

  2.34. สร้างตัวแปร Dimensionality Reduction แบบ LDA โดยกำหนด n_components = 2

  2.35. ดำเนินการ LDA โดยใช้ X_train, y_train เป็นตัว fit และ X_test เป็น transform

  2.36. สร้าง Visualization แบบ Clustering ด้วย LDA ทั้งสองแกน

  2.37. สร้างโมเดลแบบ Support Vector Machine ด้วย Components จาก LDA
(ข้อ 38-40 ใช้โมเดลจากข้อ 37)

  2.38. สร้าง countplot ของค่าที่ทำนายโดย Support Vector Machine

  2.39. วัดผลโมเดล SVM โดยใช้ confusion matrix

  2.40. ประเมินผลโมเดล SVM ด้วยคะแนน Accuracy, F1 score, Recall, Precision ทั้งแบบ Micro, Macro

  2.41. ทำ Hyperparameter tuning ด้วย GridSearchCV กับ SVM ด้วย Components จาก LDA

  2.42. วัดผลโมเดล SVM หลัง Hyperparameter tuning ด้วย confusion matrix

  2.43. ประเมินผลโมเดล SVM หลัง Hyperparameter tuning ด้วยคะแนน Accuracy, F1 score, Recall, Precision ทั้งแบบ Micro, Macro

  2.44. สร้างโมเดลแบบ Random Forest ด้วย Components จาก LDA
(ข้อ 45-47 ใช้โมเดลจากข้อ 44)

  2.45. สร้าง countplot ของค่าที่ทำนายโดย RF

  2.46. วัดผลโมเดล RF โดยใช้ confusion matrix

  2.47. ประเมินผลโมเดล RF ด้วยคะแนน Accuracy, F1 score, Recall, Precision ทั้งแบบ Micro, Macro

  2.48. Hyperparameter tuning ด้วย GridSearchCV กับ RF ด้วย Components จาก LDA

  2.49. วัดผลโมเดล Random Forest หลัง Hyperparameter tuning ด้วย confusion matrix 

  2.50. ประเมินผลโมเดล RF หลัง Hyperparameter tuning ด้วยคะแนน Accuracy, F1 score, Recall, Precision ทั้งแบบ Micro, Macro

  2.51. สร้างตัวแปร Dimensionality Reduction แบบ PCA โดยกำหนด n_components = 2

  2.52. ดำเนินการ PCA โดยใช้ X_train เป็นตัว fit และ X_test เป็น transform
    52.1 ทำ DataFrame วัดอิทธิพลของฟีเจอร์เก่าต่อ Components ใหม่ที่ PCA สร้างขึ้น
    52.2 ทำ Heatmap ของข้อ 52.1

  2.53. ทำ Clustering Visualization ของ 2 Components จาก PCA ต่อผลลัพธ์ทั้ง 3 Classes

  2.54. สร้างโมเดลแบบ Support Vector Machine ด้วย Components จาก PCA
(ข้อ 55-57 ใช้โมเดลจากข้อ 54)

  2.55. สร้าง countplot ของค่าที่ทำนายโดย Support Vector Machine

  2.56. วัดผลโมเดล SVM โดยใช้ confusion matrix

  2.57. ประเมินผลโมเดล SVM ด้วยคะแนน Accuracy, F1 score, Recall, Precision ทั้งแบบ Micro, Macro

  2.58. ทำ Hyperparameter tuning ด้วย GridSearchCV กับ SVM ด้วย Components จาก PCA

  2.59. วัดผลโมเดล SVM หลัง Hyperparameter tuning ด้วย confusion matrix

  2.60. ประเมินผลโมเดล SVM หลัง Hyperparameter tuning ด้วยคะแนน Accuracy, F1 score, Recall, Precision ทั้งแบบ Micro, Macro

  2.61. สร้างโมเดลแบบ Random Forest ด้วย Components จาก PCA
(ข้อ 62-64 ใช้โมเดลจากข้อ 61)

  2.62. สร้าง countplot ของค่าที่ทำนายโดย RF

  2.63. วัดผลโมเดล RF โดยใช้ confusion matrix

  2.64. ประเมินผลโมเดล RF ด้วยคะแนน Accuracy, F1 score, Recall, Precision ทั้งแบบ Micro, Macro

  2.65. ทำ Hyperparameter tuning ด้วย GridSearchCV กับ RF ด้วย Components จาก PCA

  2.66. วัดผลโมเดล RF หลัง Hyperparameter tuning ด้วย confusion matrix

  2.67. ประเมินผลโมเดล RF หลัง Hyperparameter tuning ด้วยคะแนน Accuracy, F1 score, Recall, Precision ทั้งแบบ Micro, Macro

  2.68. ทำ Data Visualization ของทุกโมเดล (ก่อน hyperparameter tuning) ที่ทำมา โดยใช้ Seaborn โดยให้แกน X เป็น ชื่อวิธีการ เช่น (RF + PCA) แกน Y เป็นคะแนน กำหนดให้ hue เป็น Acc, F1 Score, Precision, Recall (ใช้ Macro)

  2.69. ทำ Data Visualization ของทุกโมเดล (หลัง hyperparameter tuning) ที่ทำมา โดยใช้ Seaborn โดยให้แกน X เป็น ชื่อวิธีการ เช่น (RF + PCA) แกน Y เป็นคะแนน กำหนดให้ hue เป็น Acc, F1 Score, Precision, Recall (ใช้ Micro)

  2.70. ทำ Data Visualization ของโมเดล SVM + LDA, SVM + PCA, RF + LDA และ RF + PCA โดยให้ชื่อโมเดลเป็นแกน X และ คะแนน Acc เป็นแกน Y โดยใช้ plotly 















