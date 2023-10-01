fake_politics_data = ' '.join(merged_data[(merged_data['subject'] == 'politics') & (merged_data['label'] == 'fake')]['clean_text'])
total_fake_news = ' '.join(merged_data[merged_data['label'] == 'fake']['clean_text'])
fake_politics_data[0:500]
total_fake_news[0:500]
wordcloud = WordCloud(width=800, height=400).generate(fake_politics_data)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud for Fake Politics News')
plt.show()