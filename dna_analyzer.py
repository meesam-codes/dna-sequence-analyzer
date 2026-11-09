def read_sequence(filename):
    try:
        with open(filename, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        print("file not found! plz check file again.")
        return ""

seq = read_sequence("input_sequence.txt")
print("sequences is read:", seq)

def count_bases(seq):
    counts = {
        "A" : seq.count("A"),
        "T" : seq.count("T"),
        "G" : seq.count("G"),
        "C" : seq.count("C")
    }
    return counts
bases = count_bases(seq)
print("base counts:", bases)

def gc_content(seq):
    if len(seq) == 0:
        return 0.0
    g_c_count = seq.count("G") + seq.count("C")
    percentage = g_c_count / len(seq) * 100
    return percentage
def to_rna(seq):
    return seq.replace("T" , "U")
gc_val = gc_content(seq)
rna_seq = to_rna(seq)

if gc_val > 60:
    classification = "high"
elif gc_val >= 40:
    classification = "normal"
else:
    classification = "low"
print(f"GC Content: {gc_val: .2f}% ({classification})")
print("RNA Version:", rna_seq)
total_len = len(seq)
most_frequent = max(bases, key=bases.get)

with open("analysis_report.txt", "w") as report:
    report.write("--- DNA ANALYSIS REPORT ---\n")
    report.write(f"ORIGINAL DNA: {seq}\n")
    report.write(f"TOTAL LENGTH: {total_len}\n")
    report.write(f"Base counts: {bases}\n")
    report.write(f"Most frequent base: {most_frequent}\n")
    report.write(f"GC Content: {gc_val: .2f}% ({classification})\n")
    report.write(f"RNA version: {rna_seq}\n")

print("Analysis complete. See analysis_report.txt for results.")