
def scan_report(res):
    with open("Output/Scan_report.txt","w") as file:
        file.write(f"{'PORT':<11} | {'STATUS':<22} | {'SERVICE':<15} | {'TIME':<14}\n")
        for p,st,ser,t in res:
            file.write(f"Port no: {p} | {st:<22} | {ser:<15} | {t:.6f}\n")
            
        
