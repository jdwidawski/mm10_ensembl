"""Process ensembl annotation using comma delimetered chromosome files as inputs
and outputs relevand information in a .csv table

Input files have to be previously unpacked


Source:
    ftp://ftp.ensembl.org/pub/release-99/embl/mus_musculus/ (Latest genome release)


"""

import pandas as pd

class process_file():
    def __init__(self, chr_id):

        chr_id = str(chr_id)
        self.chr_id = chr_id

        base = "Mus_musculus.GRCm38.99.chromosome"

        with open(base+"_"+chr_id+".txt", "rt") as inp:
            input_file = inp.readlines()
            filestr = ''.join(input_file).replace("\n", "").replace("FT", "")
            input_list = [line for line in filestr.split("  gene  ") if "ENSMUS" in line]

        big_list = []
        for line in input_list:
            start, end = self.get_positions(line)
            ensembl_id = self.get_ensembl_id(line)
            gene_name = self.get_locus_tag(line)
            note = self.get_note(line)
            big_list.append([ensembl_id, gene_name, start, end, note])

        temp_dataframe = self.make_dataframe(big_list)

        self.temp_dataframe = temp_dataframe
        self.return_dataframe()


    def get_positions(self,line):
        positions_str = line.strip().split(" ")[0].strip()

        if 'complement' in positions_str:
            positions_str = positions_str.replace("complement(", "").replace(")","").strip()

        start = positions_str.split("..")[0]
        end = positions_str.split("..")[1]

        return start, end

    def get_ensembl_id(self,line):
        ensembl_str = line.split("/gene=")[1].split(" ")[0].strip()

        if len(ensembl_str) == 0:
            ensembl_str = "n/a"

        return ensembl_str

    def get_locus_tag(self,line):
        locus_str = line.split('/locus_tag="')[1].split('"')[0].strip()

        if len(locus_str) == 0:
            locus_str = "n/a"

        return locus_str

    def get_note(self,line):
        note_str = line.split('/note="')[1]

        if "[Source:" in note_str.strip()[:50]:
            note_str = note_str.split('[Source:')[0].strip()

        elif "transcript_id" in note_str[:15]:
            note_str = "n/a"

        else:
            note_str = note_str.split('  ')[0].strip()


        if len(note_str) == 0:
            note_str = "n/a"

        return note_str

    def make_dataframe(self, big_list):

        ensembl_df = pd.DataFrame(big_list)
        ensembl_df.columns = ["ensembl_id", "gene_name", "start", "end", "note"]

        if self.chr_id == "nonchromosomal":
            ensembl_df.insert(0, "chr", [self.chr_id for x in range(0,len(ensembl_df))])
        else:
            ensembl_df.insert(0, "chr", ['chr'+self.chr_id for x in range(0,len(ensembl_df))])

        return ensembl_df

    def return_dataframe(self):
        return self.temp_dataframe


def call_class(pipeline, file_name):
    all_data = []
    try:
        from tqdm.auto import tqdm

        for chrname in tqdm(pipeline):
            all_data.append(process_file(chrname).return_dataframe())
            full_dataframe = pd.concat(all_data).reset_index(drop=True)
            full_dataframe.to_csv(file_name, encoding="utf-8")

    except ModuleNotFoundError:
        for chrname in pipeline:
            all_data.append(process_file(chrname).return_dataframe())
            full_dataframe = pd.concat(all_data).reset_index(drop=True)
            full_dataframe.to_csv(file_name, encoding="utf-8")

    print(f"\nDone, you can find the table saved as -->  {file_name}  <-- in your directory")

if __name__ == "__main__":
    pipeline = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, "MT", 'X', 'Y', 'nonchromosomal']
    call_class(pipeline, "ensembl_data.csv")