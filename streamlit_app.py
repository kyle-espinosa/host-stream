import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import squarify
import pandas as pd

st.title("Group Number: 7")
st.header("Section: BM3")

st.write(
    "- ESPINOSA \n"
    "- FALLORAN \n"
    "- LEYVA \n"
    "- PECENIO \n"
    "- YOUNG \n"
)

df = pd.read_csv('csv1/Electronic_sales_Sep2023-Sep2024.csv')
    
    
st.write(df)


df_info = df.info()
missing_values = df.isna().sum()
descriptive_stats = df.describe()
df_info, missing_values, descriptive_stats

st.write("Data columns (total {} columns):".format(df.shape[1]))
info_df = pd.DataFrame({
    'Column': df.columns,
    'Non-Null Count': df.notnull().sum(),
    'Dtype': df.dtypes
})
st.dataframe(info_df)

# Graph 1: Sales Distribution by Product Type - Young

plt.figure(figsize=(12, 6))
sns.countplot(data=df, 
              x='Product Type', 
              hue='Product Type', 
              palette='viridis', 
              order=df['Product Type'].value_counts().index, 
              legend=False)

plt.title('Sales Distribution by Product Type')
plt.xlabel('Product Type')
plt.ylabel('Number of Sales')
plt.xticks(rotation=45)
st.pyplot(plt)
plt.clf()
st.write("Based on the graph, the product type with the highest sales is smartphones, indicating strong demand, while the least sold product type is headphones, suggesting potential areas for improvement in marketing or product visibility.")


# Graph 2: Total Sales Over Time - Young
df['Purchase Date'] = pd.to_datetime(df['Purchase Date'], errors='coerce')

sales_over_time = df.groupby('Purchase Date')['Total Price'].sum().reset_index()

plt.figure(figsize=(14, 7))
sns.lineplot(data=sales_over_time, x='Purchase Date', y='Total Price', marker='o', color='blue')
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid()
st.pyplot(plt)
plt.clf()
st.write("The graph shows a sharp increase in total sales around January 2024, with sales rising from below 100,000 to fluctuating mostly between 150,000 and 250,000. Prior to January, sales were more stable but lower, while after January, the data exhibits higher variability with frequent spikes and dips. This suggests a significant event or change around the start of 2024 that boosted sales but also caused more irregular patterns.")


# Graph 3: Age Demographic - Leyva
colors = ['skyblue', 'lightgreen', 'salmon', 'orange', 'plum', 'mediumpurple']
bins = [18, 30, 40, 50, 60, 70, 80]
labels = ['19-30', '31-40', '41-50', '51-60', '61-70', '71-80']

df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
age_distribution = df['Age Group'].value_counts()

plt.pie(age_distribution, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Age Demographic')
st.pyplot(plt)
plt.clf()
st.write("The pie chart shows the proporotion of each age group in the given dataset. Based on an initial view of the chart, the customers that purchase in the electronics market are almost evenly bought throughout each age range. The largest portion being customers aged 19 to 30. The inverse would be the elderly customers from ages 71 to 80. The dataset does not have customers aged 18 and below.")

# Graph 4: Number of Customers by Shipping Type (Espinosa)
plt.figure(figsize=(12, 6))
shipping_types = df['Shipping Type'].value_counts()
sns.barplot(x=shipping_types.index, y=shipping_types.values, hue=shipping_types.index, palette='cividis', legend=False)
plt.title('Customer Distribution by Shipping Type')
plt.xlabel('Shipping Type')
plt.ylabel('Number of Customers')
plt.xticks(rotation=45)
st.pyplot(plt)
plt.clf()
st.write("The most preferred shipping option is the Standard at 6,725 customers, leading by a huge margin. The others are in the 3,000 range, with Express at 3,366 customers, Overnight at 3,357 customers, Same Day at 3,280 customers, and Expedite at 3,272 customers. The graph entails the improvement of other shipping options for them to be a priority for the customers.")

# Graph 5: Total Amount Spent by Age Range (Espinosa)
plt.figure(figsize=(12, 6))
labels = ['19-30', '31-40', '41-50', '51-60', '61-70', '71-80']
df['Age Range'] = pd.cut(df['Age'], bins=[19, 31, 41, 51, 61, 71, 80], labels=labels)

age_range_freq = df['Age Range'].value_counts()

sns.histplot(data=df, x='Age Range', palette='cividis')
plt.title('Total Amount Spent Distribution by Age Range')
plt.xlabel('Age Range')
plt.ylabel('Total Amount Spent')
st.pyplot(plt)
plt.clf()
st.write("Based on the histogram, the total amount spent by ages 19-30 is the highest compared to the other age ranges, with a total amount spent of 3,757. On the other hand, the least total amount spent is from the age range 71-80 with a total amount spent of 2,770. The total amount spent by ages 31-70 is close to each other and is in the middle of ages 19-30 and 71-80. Respectively, 31-40 at 3,250, 41-50 at 3,188, 51-60 at 3,219, and 61-70 at 3,198. The histogram suggests either more products that can cater to those from ages 71-80 and improving the market other than those of ages 19-30 to increase the total amount spent for other age ranges.")

# Graph 6: - Leyva
loyalProdAvg = df.groupby(['Product Type', 'Loyalty Member'])['Total Price'].mean().unstack()

loyalProdAvg.plot(kind='bar', stacked=False, color=['skyblue', 'salmon'], figsize=(14,8))
plt.title('Average Purchase Value by Product Type and Loyalty Status')
plt.xlabel('Product Type')
plt.ylabel('Average Value (USD)')
plt.xticks(rotation=45)
plt.legend(title='Loyalty Status')
st.pyplot(plt)
plt.clf()
st.write("For this chart, it presents the average purchase value of each product type sold in the electronic market and segmented by whether or not the customer is a loyalty member. Notably, non-loyalty members have a slightly higher average spending than those who are. Specifically, for the products, laptops, smartphones, and smartwatches.")
st.write("This may suggest that the electronic market's loyalty program effectively increases customer spending on average.")

#Graph 7: Scatter Plot Rating vs Unit Price - Falloran
x = df['Unit Price']
y = df['Rating']

plt.scatter(x, y, color='blue')
plt.title('Rating vs Unit Price')
plt.xlabel('Unit Price ($)')
plt.ylabel('Rating')
st.pyplot(plt)
plt.clf()
st.write("The scatter plot illustrates the relationship between unit price (in dollars) and product ratings (on a scale from 1 to 5). The Scatter Plot shows that there is no clear correlation between price and rating; products with high ratings (4 or 5) are present at both low and high price points, while products with low ratings (1 or 2) are similarly scattered throughout the price range.")

#Graph 8: Sales Data Correlation Analysis - Pecenio
fig, ax = plt.subplots(figsize=(10, 6))

numeric_cols = df[['Total Price', 'Unit Price', 'Quantity', 'Age']]
corr_matrix = numeric_cols.corr()

sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, ax=ax)
ax.set_title('Sales Data Correlation Analysis Heatmap')
st.pyplot(fig)
plt.clf()
st.write("The heatmap demonstrates significant links in the sales data. There is a substantial positive association between total price and quantity, implying that larger quantities sold result in greater total sales. Similarly, unit price and total price are significantly associated, implying that more expensive things likely to generate larger total sales.")


#Graph 9: Sales Contribution - Falloran

sales_data = df.groupby('Product Type')['Total Price'].sum().reset_index()
values = sales_data['Total Price']
categories = sales_data['Product Type']

squarify.plot(sizes=values, label=categories, color=['red', 'green', 'blue', 'orange', 'purple', 'cyan'], alpha=0.7)
plt.title('Sales Contribution by Product Type')
plt.axis('off')
st.pyplot(plt)
plt.clf()
st.write("The treemap provides a visual representation of sales contributions by different product types, with each section's size reflecting its share of total sales. The largest portion of the treemap belongs to smartphones. Smartwatches and tablets follow closely, each occupying similarly sized sections. Next to it are laptops. Lastly,the smallest section belongs to headphones, indicating that they contribute the least to the overall sales distribution. Overall, smartphones dominate sales, while headphones account for the smallest portion.")

#Graph 10: Violin Plot of Total Price by Product Type
plt.figure(figsize=(12, 6))
sns.violinplot(data=df, x='Product Type', y='Unit Price', hue='Product Type', palette='muted', split=True, legend=False)
plt.title('Price Distribution by Product Type')
plt.xlabel('Product Type')
plt.ylabel('Unit Price')
plt.xticks(rotation=45)
plt.grid()
st.pyplot(plt)
plt.clf()
st.write("The violin plot depicts the distribution of unit prices across several product categories. Each segment of the violin represents the density of pricing in that category. Certain product kinds, such as Smartphone, have a broader variety of unit prices, indicating variation in pricing tactics or client willingness to pay. Other categories, such as Headphones, have a narrower price distribution, indicating more consistent pricing throughout their products. This graphic can be used to identify pricing trends and develop pricing strategy for each product category.")


st.header("Conclusion")
st.markdown("**Dominance of Smartphones**: The data shows that smartphones dominate sales, with a clear indication of strong consumer demand in this category. This trend suggests that smartphones are not just popular but are also essential items for many consumers.")
st.markdown("**Shipping Preferences**: The majority choice for Standard shipping reflects consumer behavior that favors convenience and reliability. This preference illustrates that shipping options play a crucial role in the overall customer experience, as most customers seem to prioritize this method over faster alternatives.")
st.markdown("**Customer Loyalty and Spending**: Loyalty program members exhibit only slightly lower average spending than non-loyalty members. This could suggest that while loyalty initiatives may not drastically affect spending patterns, they still ensure steady revenue from a significant portion of the customer base, particularly for higher-ticket items like smartphones and laptops.")
st.markdown("**Quality Across Price Ranges**: The lack of a clear correlation between unit price and product ratings shows that consumers are willing to find value in products across different price points. This observation implies that customers assess quality based on factors beyond just price, highlighting the importance of perceived value.")
st.markdown("**Encouraging Bulk Purchases**:  The positive relationship between total price and quantity sold indicates that consumers are likely to buy more when they perceive a higher total cost. This observation suggests a trend in buying behavior that aligns with the idea that larger quantities can lead to greater satisfaction.")

