import pandas as pd


def clean(contact_info_file,other_info_file):
    df1 = pd.read_csv(contact_info_file)
    df2 = pd.read_csv(other_info_file)
    df2.rename(columns=({"id": "respondent_id"}), inplace=True)
    df = pd.merge(df1, df2, on='respondent_id', how='outer')
    df = df.dropna(axis=0)
    df = df[df['job'].notnull()]
    df = df.loc[~(df['job'].str.contains('Insurance')) & (~df['job'].str.contains('insurance'))]
    return df

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('contact_info_file', help='Respondent contact file (CSV)')
    parser.add_argument('other_info_file', help='Respondent other file (CSV)')
    parser.add_argument('output_file', help='Cleaned data file (CSV)')
    args = parser.parse_args()

    cleaned = clean(args.contact_info_file,args.other_info_file)
    cleaned.to_csv(args.output_file, index=False)