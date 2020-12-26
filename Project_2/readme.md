### Codecamp #รุ่น3
  1. Waranya Thamsritip

  2.1. โหลด csv เข้าไปใน Python Pandas

  2.2. เขียนโค้ดแสดง หัว10แถว ท้าย10แถว และสุ่ม10แถว

  2.3. ใช้ info และ describe อธิบายข้อมูลเบื้องต้น

  2.4. ใช้ pairplot ดูความสัมพันธ์เบื้องต้น

  2.5. ใช้ displot เพื่อดูการกระจายของแต่ละคอลัมน์

  2.6. สร้าง countplot ของสินค้าแต่ละชนิด และ ปรับแกนให้เหมาะสม

  2.7. ใช้ heatmap ดูความสัมพันธ์ของคอลัมน์ที่สนใจ

  2.8. หา Correlation ของทั้ง Dataframe

  2.9. สร้าง scatter plot ของความสัมพันธ์ที่มี Correlation สูงสุด

  2.10. สร้าง scatter plot ของความสัมพันธ์ที่มี Correlation ต่ำสุด

  2.11. เช็คข้อมูลของทุก category columns ดูว่ามีข้อมูลที่ผิดเพี้ยนไหม หากมีแก้ไขตามความเหมาะสม

  2.12. สร้าง countplot ของ Outlet แต่ละชนิด โดยแบ่งสีจาก Item_fat_content

  2.13. สร้าง scatterplot figure ขนาด 12x8 ให้แกน X เป็น Item_MRP แกน Y เป็น Target แบ่งประเภทด้วย Item_fat_content ขนาดเท่ากับน้ำหนัก ลงสี palette 

  2.14. สร้าง box plot ของ target กับชนิดสิ่งของ 

  2.15. สร้าง box plot ของ target กับขนาดของ outlet

  2.16. สร้าง box plot ของ target กับชนิดของ outlet

  2.17. สร้าง box plot ของ target กับชนิดของ location ของ outlet

  2.18. สร้าง box plot ของ target กับ Item_fat_content

  2.19. สร้าง box plot ของ Item_fat_content กับ Item_MRP

  2.20. สร้าง box plot ของ item_fat_content กับน้ำหนักของสินค้า

  2.21. ใช้ plotly พล็อต pie chart ของ target กับชนิดของสินค้า

  2.22. หาราคาเฉลี่ยของสินค้าแต่ละ ID

  2.23. ใช้ plotly พล็อต scatter plot โดยให้แกน X เป็น ID ของสินค้า 10 ตัวแรก Y เป็นยอดขาย และขนาดเท่ากับน้ำหนักของสินค้า และสีเท่ากับ Item_Visibility

  2.24. แสดง dataframe ที่ outlet_type มีแค่ Grocery Store โดยใช้ 1) pandas index และ 2) groupby

  2.25. แสดง dataframe ที่ ชนิดของสินค้าคือน้ำอัดลมและขนาดของ outlet คือเล็ก (hint: ใช้ bitwise operator)

  2.26. bitwise operator ต่างกับ logical operator อย่างไร (อ้างอิงจากข้อ 25 ได้)

  2.27. เช็คและแปลงข้อมูลให้อยู่ในรูปแบบที่เหมาะสม (hint: แปลง data dtype บางคอลัมน์)

  2.28. สร้าง heatmap แสดงข้อมูลที่หายไปของแต่ละ column (สามารถย้อนไปดู titanic dataset ได้)

  2.29. เช็คว่ามีข้อมูลที่หายไปไหม ถ้าเป็นตัวเลขให้ใส่ด้วยค่าเฉลี่ย ถ้าเป็น Categorical ให้ใส่ด้วย Category อันที่มีความถี่สูงที่สุด

  2.30. drop ข้อมูลที่คิดว่าไม่มีผลต่อยอดขายออก และให้เหตุผลว่าทำไม

  2.31. Print ยอดขายที่มากสุดและน้อยสุดใน dataframe

  2.32. ทำ dummies สำหรับ Categorical data และ สร้าง train/test split ด้วย 80:20 ratio

  2.33. สร้างโมเดลแบบ Simple Linear Regression โดยใช้ Item_MRP เป็น independent variable เพียงตัวเดียว

  2.34.  แสดงค่า intercept และ coefficient พร้อมกับอธิบายทั้งสองค่าว่าคืออะไรและหมายความว่าอย่างไร

  2.35. ทดสอบโมเดลวัดค่า MAE, MSE, RMSE และ R2

  2.36. สร้าง distribution plot ของผลต่างระหว่าง y_test กับ predicted results และอธิบายความหมาย

  2.37. สร้าง scatter plot และ prediction line ของ simple linear regression

  2.38. สร้างโมเดลแบบ Support Vector Regression แบบ rbf โดยใช้ Item_MRP เป็น independent variable เพียงตัวเดียว (ทำข้อ 39 ก่อน)

  2.39.  ใช้ Standard Scaler ในการทำ feature scaling ทั้งแกน X และ Y

  2.40. ทดสอบโมเดลวัดค่า MAE, MSE, RMSE และ R2

  2.41. สร้าง distribution plot ของผลต่างระหว่าง y_test กับ predicted results และอธิบายความหมาย

  2.42. สร้าง scatter plot และ prediction line ของ RBF support vector regressor

  2.43. สร้างโมเดลแบบ Multiple Linear Regression โดยใช้ทุก features (ที่เหลืออยู่)

  2.44.  แสดงค่า intercept และ coefficient ของทั้งหมด

  2.45. ทดสอบโมเดลวัดค่า MAE, MSE, RMSE และ R2

  2.46. สร้าง distribution plot ของผลต่างระหว่าง y_test กับ predicted results และอธิบายความหมาย

  2.47. สร้าง dataframe เปรียบเทียบ ยอดขายจริงกับการทำนาย

  2.48. หา Correlation จาก dataframe ข้อ 47

  2.49.  สร้างโมเดลแบบ Support Vector Regression แบบ rbf โดยใช้ทุก features

  2.50. ทดสอบโมเดลวัดค่า MAE, MSE, RMSE และ R2

  2.51. สร้าง distribution plot ของผลต่างระหว่าง y_test กับ predicted results และอธิบายความหมาย

  2.52. สร้าง dataframe เปรียบเทียบ ยอดขายจริงกับการทำนาย

  2.53. หา Correlation จาก dataframe ข้อ 52

  2.54.  สร้างโมเดลแบบ Decision Tree Regression โดยใช้ทุก features

  2.55. ทดสอบโมเดลวัดค่า MAE, MSE, RMSE และ R2

  2.56. สร้าง distribution plot ของผลต่างระหว่าง y_test กับ predicted results

  2.57. สร้าง dataframe เปรียบเทียบ ยอดขายจริงกับการทำนาย

  2.58. หา Correlation จาก dataframe ข้อ 57

  2.59.  สร้างโมเดลแบบ Random Forest Regression โดยใช้ทุก features

  2.60. ทดสอบโมเดลวัดค่า MAE, MSE, RMSE และ R2

  2.61. สร้าง distribution plot ของผลต่างระหว่าง y_test กับ predicted results

  2.62. สร้าง dataframe เปรียบเทียบ ยอดขายจริงกับการทำนาย

  2.63. หา Correlation จาก dataframe ข้อ 62

  2.64.  สร้างโมเดลแบบ Multiple Linear Regression โดยใช้ทุก features และใช้ Standard Scaler ทั้ง dependent และ independent variables

  2.65. ทดสอบโมเดลวัดค่า MAE, MSE, RMSE และ R2

  2.66. สร้าง distribution plot ของผลต่างระหว่าง y_test กับ predicted results

  2.67. สร้าง dataframe เปรียบเทียบ ยอดขายจริงกับการทำนาย

  2.68. หา Correlation จาก dataframe ข้อก่อนหน้า

  2.69.  สร้างโมเดลแบบ Support Vector Regression แบบ rbf โดยใช้ทุก features และใช้ Standard Scaler กับทั้ง dependent และ independent variables

  2.70. ทดสอบโมเดลวัดค่า MAE, MSE, RMSE และ R2

  2.71. สร้าง distribution plot ของผลต่างระหว่าง y_test กับ predicted results

  2.72. สร้าง dataframe เปรียบเทียบ ยอดขายจริงกับการทำนาย

  2.73. หา Correlation จาก dataframe ข้อก่อนหน้า

  2.74.  สร้างโมเดลแบบ Decision Tree Regression โดยใช้ทุก features และใช้ Standard Scaler กับทั้ง dependent และ independent variables

  2.75. ทดสอบโมเดลวัดค่า MAE, MSE, RMSE และ R2

  2.76. สร้าง distribution plot ของผลต่างระหว่าง y_test กับ predicted results

  2.77. สร้าง dataframe เปรียบเทียบ ยอดขายจริงกับการทำนาย

  2.78. หา Correlation จาก dataframe ข้อก่อนหน้า

  2.79.  สร้างโมเดลแบบ Random Forest Regression โดยใช้ทุก features และใช้ Standard Scaler ทั้ง dependent และ independent variables

  2.80. ทดสอบโมเดลวัดค่า MAE, MSE, RMSE และ R2

  2.81. สร้าง distribution plot ของผลต่างระหว่าง y_test กับ predicted results

  2.82. สร้าง dataframe เปรียบเทียบ ยอดขายจริงกับการทำนาย

  2.83. หา Correlation จาก dataframe ข้อก่อนหน้า

  2.84.  สร้าง bar chart แสดงค่า RMSE ของทุกผลลัพธ์ทั้งหมดที่ทำมา ยกเว้น 1 indepedent variable (สองอันแรก) แล้วเปรียบเทียบว่า Model มีประสิทธิภาพมากที่สุด

  2.85. สร้าง bar chart แสดงค่า r2_score ของทุกผลลัพธ์ทั้งหมดที่ทำมา ยกเว้น 1 indepedent variable (สองอันแรก) แล้วเปรียบเทียบว่า Model มีประสิทธิภาพมากที่สุด




















