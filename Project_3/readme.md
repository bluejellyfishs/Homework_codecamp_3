### Codecamp #รุ่น3
  1. Waranya Thamsritip

  2.1. โหลด csv เข้าไปใน Python Pandas

  2.2. เขียนโค้ดแสดง หัว10แถว ท้าย10แถว และสุ่ม10แถว

  2.3. ใช้ info และ describe อธิบายข้อมูลเบื้องต้น

  2.4. ใช้ pairplot ดูความสัมพันธ์เบื้องต้น

  2.5. หาจำนวนของค่า unique ของแต่ละ column

  2.6. ลบ Rownumber, customerID คอลัมน์

  2.7. สร้าง Distribution plot ของแต่ละคอลัมน์ 

  2.8. เฉพาะคอลัมน์ Balance ให้ทำ distplot ที่ไม่รวม Balance=0 ด้วย

  2.9. สร้าง countplot ของ Geography

  2.10. สร้าง countplot ของ Gender

  2.11. เช็คว่ามีนามสกุลที่แตกต่างกันทั้งหมดกี่นามสกุลและมีอะไรบ้าง

  2.12. เช็คว่ามีนามสกุลที่แตกต่างกันทั้งหมดกี่นามสกุลและมีอะไรบ้าง (เฉพาะนามสกุลที่ซ้ำ, ความถี่มากกว่า 1)

  2.13. สร้าง barplot ให้กับ 15 นามสกุลแรกที่มีการซ้ำมากที่สุดเรียงจากซ้ายไปกว่า และขวามาซ้าย

  2.14. หา Correlation ของ DataFrame

  2.15. สร้าง heatmap จาก Correlation ของ DataFrame

  2.16. สร้าง scatterplot ของ Balance กับ EstimatedSalary (จากสมมติฐานของเราว่าคนเงินเดือนเยอะ เงินฝากน่าจะเยอะด้วย)

  2.17. สร้าง scatterplot ของ Balance กับ EstimatedSalary เฉพาะคู่ที่ค่าของ Balance > 0 

  2.18. สร้าง scatterplot ของอายุกับเงินเดือนโดยประมาณ (จากสมมติฐานของเราว่าคนอายุเยอะ ทำงานนาน เงินเดือนน่าจะสูงขึ้นด้วย)

  2.19. สร้าง countplot ของ Geography แบ่งสีด้วยเพศ

  2.20. บอกจำนวนของแต่ละเพศในภูมิภาคที่ต่างกัน

  2.21. ดู % ของลูกค้าที่ churn 

  2.22. ใช้ plotly พล็อต pie chart ของผลรวมของจำนวนลูกค้าที่ churn ในแต่ละภูมิภาค

  2.23. ใช้ plotly พล็อต bar chart ของผลรวมของจำนวนลูกค้าที่ churn ในแต่ละภูมิภาค

  2.24. หาจำนวน % ของลูกค้าที่ churn ในแต่ละภูมิภาค (คิดในภูมิภาคตัวเอง)

  2.25. ใช้ plotly พล็อต pie chart ของอัตราส่วนของ % ของจำนวนลูกค้าที่ churn ในแต่ละภูมิภาค (ไม่เหมือนข้อ 22)

  2.26. ใช้ plotly สร้าง distplot ของกลุ่มอายุลูกค้าที่ churn และระบุช่วงอายุใดมีการ churn มากที่สุด

  2.27. ใช้ plotly สร้าง bubble plot ให้แกน X เป็นช่วงอายุ 18-27 แกน y เป็นเงินเดือนเฉลี่ยของช่วงอายุ ขนาดเป็นยอดเงินคงเหลือเฉลี่ย และสีเป็น CreditScore

  2.28. ใช้ plotly สร้าง barplot ของ % ของลูกค้าที่ churn ในแต่ละค่าของ NumOfProduct ใส่ชื่อแกนและชื่อกราฟให้เหมาะสม (อธิบายว่า Data Insight ที่ได้จากกราฟนี้สมเหตุสมผลหรือไม่อย่างไร)

  2.29. ใช้ plotly สร้าง barplot หา % การ churn ของแต่ละเพศ

  ต่อมาเป็นการจัดการกับ Outliers

  2.30. ใช้ boxplot ตรวจหา outliers ของแต่ละ feature

  2.31. Feature ที่มีค่าที่เกินขอบเขตบน (upper fence) ให้เปลี่ยนค่าเหล่านั้นให้เท่าขอบเขตบน ถ้าต่ำกว่าขอบเขตล่าง (lower fence) ให้ปรับค่าเหล่านั้นให้เท่ากับขอบเขตล่าง

  2.32. เปลี่ยนชื่อ column จาก Exited เป็น churn

  2.33. ลบฟีเจอร์นามสกุล

  2.34. สร้าง dummies ให้ Categorical columns พร้อมทั้งจัดการ 
Multi-collinearity

  2.35. สร้าง train/test split ด้วย 80:20 ratio

  2.36. สร้างโมเดลแบบ Logistic Regression

  2.37. สร้าง countplot ของค่าที่ทำนายโดย Logistic Regression

  2.38. วัดผลโมเดล Logistic Regression โดยใช้ confusion matrix และ ประเมินผลด้วยคะแนน Accuracy, F1 score, Recall, Precision

  2.39. สร้างโมเดลแบบ K-Nearest Neighbours

  2.40. สร้าง countplot ของค่าที่ทำนายโดย KNN

  2.41. วัดผลโมเดล KNN โดยใช้ confusion matrix และ ประเมินผลด้วยคะแนน Accuracy, F1 score, Recall, Precision

  2.42. สร้างโมเดลแบบ Support Vector Machine

  2.43. สร้าง countplot ของค่าที่ทำนายโดย SVM

  2.44. วัดผลโมเดล SVM โดยใช้ confusion matrix และ ประเมินผลด้วยคะแนน Accuracy, F1 score, Recall, Precision

  2.45. ให้เหตุผลว่าทำไมโมเดล SVM ถึงมีค่า F1 Score, Recall, Precision เป็น 0 แต่ Accuracy ไม่ใช่

  2.46. สร้างโมเดล Naïve Bayes

  2.47. สร้าง countplot ของค่าที่ทำนายโดย Naïve Bayes

  2.48. วัดผลโมเดล Naïve Bayes โดยใช้ confusion matrix และ ประเมินผลด้วยคะแนน Accuracy, F1 score, Recall, Precision

  2.49.  สร้างโมเดลแบบ Decision Tree

  2.50. สร้าง countplot ของค่าที่ทำนายโดย Decision Tree

  2.51. วัดผลโมเดล Decision Tree โดยใช้ confusion matrix และ ประเมินผลด้วยคะแนน Accuracy, F1 score, Recall, Precision

  2.52. สร้างโมเดลแบบ Random Forest

  2.53. สร้าง countplot ของค่าที่ทำนายโดย Random Forest

  2.54. วัดผลโมเดล Random Forest โดยใช้ confusion matrix และ ประเมินผลด้วยคะแนน Accuracy, F1 score, Recall, Precision

  2.55. ใช้ plotly ทำ barplot เปรียบเทียบค่า Accuracy, F1 score, Recall, Precision ของแต่ละโมเดล

  2.56. ทำ Normalization ให้ Dataset สำหรับ SVM โมเดล และเทรนโมเดล SVM ใหม่

  2.57. สร้าง countplot ของค่าที่ทำนายโดย SVM

  2.58. วัดผลโมเดล SVM โดยใช้ confusion matrix และ ประเมินผลด้วยคะแนน Accuracy, F1 score, Recall, Precision แล้วพิจาณาว่าผลลัพธ์ดีขึ้นไหม

  2.59. ใช้ GridSearch ทำ Hyperparameter tuning ให้ SVM โดยใช้ข้อมูลที่ Normalized แล้ว

  2.60. สร้าง countplot ของค่าที่ทำนายโดย SVM ที่ทำ Hyperparameter tuning + Normalization แล้ว

  2.61. วัดผลโมเดล SVM โดยใช้ confusion matrix และ ประเมินผลด้วยคะแนน Accuracy, F1 score, Recall, Precision แล้วพิจาณาว่าผลลัพธ์ดีขึ้นไหม

  2.62. ใช้ GridSearch ทำ Hyperparameter tuning ให้ Random Forest
  
  2.63. สร้าง countplot ของค่าที่ทำนายโดย RF ที่ทำ Hyperparameter tuning 

  2.64. วัดผลโมเดล RF โดยใช้ confusion matrix และ ประเมินผลด้วยคะแนน Accuracy, F1 score, Recall, Precision แล้วพิจาณาว่าผลลัพธ์ดีขึ้นไหม

  2.65. สร้าง barplot วัดค่า Accuracy ของทุกโมเดลที่ทำมา

  2.66. สร้าง barplot วัดค่า F1Score ของทุกโมเดลที่ทำมา

  2.67. สร้าง barplot วัดค่า Precision ของทุกโมเดลที่ทำมา

  2.68. สร้าง barplot วัดค่า Recall ของทุกโมเดลที่ทำมา















