import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os
csv_path = r'''C:\Users\elton\Downloads\archive\Student_Placement_Skills_2025.csv'''
out_dir = r'''C:\Users\elton\projects\ai-data-copilot-pencil\analysis'''

df = pd.read_csv(csv_path)
# Basic counts
n = len(df)
placed = df['Placement_Offer'].str.strip().str.lower().map({'yes':1,'no':0})
placement_rate = placed.mean()
# Numeric conversions
df['Placed'] = placed
# summary stats
summary = {
    'rows': int(n),
    'placement_rate': float(placement_rate),
    'avg_CGPA': float(df['CGPA'].mean()),
    'avg_tech_skill': float(df['Technical_Skills_Score_100'].mean()),
    'avg_comm_skill': float(df['Communication_Skills_Score_100'].mean()),
    'avg_aptitude': float(df['Aptitude_Test_Score_100'].mean())
}
# By degree
by_degree = df.groupby('Degree').agg(
    count=('Student_ID','count'),
    placed_pct=('Placed','mean'),
    avg_CGPA=('CGPA','mean'),
    avg_salary=('Salary_Offered_USD', lambda s: s[df['Placed']==1].mean() if len(s[df['Placed']==1])>0 else None)
).reset_index()

# Correlations
numcols = ['CGPA','Internships_Count','Projects_Count','Certifications_Count','Technical_Skills_Score_100','Communication_Skills_Score_100','Aptitude_Test_Score_100','Placed','Salary_Offered_USD']
corr = df[numcols].corr()

# Save summary
with open(os.path.join(out_dir,'summary.json'),'w') as f:
    json.dump({'summary':summary,'by_degree':by_degree.to_dict(orient='records')},f,indent=2,default=lambda x: None)
with open(os.path.join(out_dir,'summary.txt'),'w') as f:
    f.write('Rows: %d\n' % n)
    f.write('Placement rate: %.2f%%\n' % (placement_rate*100))
    f.write('Average CGPA: %.2f\n' % summary['avg_CGPA'])
    f.write('\nBy degree:\n')
    f.write(by_degree.to_string(index=False))

# Plots
sns.set(style='whitegrid')
plt.figure(figsize=(8,5))
ax = (df.groupby('Degree')['Placed'].mean().sort_values(ascending=False)*100).plot(kind='bar', color='steelblue')
ax.set_ylabel('Placement Rate (%)')
plt.tight_layout()
plt.savefig(os.path.join(out_dir,'placement_rate_by_degree.png'))
plt.close()

plt.figure(figsize=(8,5))
sns.boxplot(x='Degree', y='Salary_Offered_USD', data=df[df['Placed']==1])
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(out_dir,'salary_by_degree_box.png'))
plt.close()

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm')
plt.tight_layout()
plt.savefig(os.path.join(out_dir,'correlation_heatmap.png'))
plt.close()

# Top features correlation with placement
corr_placed = corr['Placed'].drop('Placed').abs().sort_values(ascending=False)
with open(os.path.join(out_dir,'top_features.txt'),'w') as f:
    f.write('Top correlated numeric features with placement (abs corr):\n')
    f.write(corr_placed.to_string())

print('Analysis done')
