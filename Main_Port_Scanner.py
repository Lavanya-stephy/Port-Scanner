import Scanner
import color
import report

val=input("Enter Host name or IP address: ")
ip=Scanner.host_name(val)


rg=list(map(int,input("Enter your range (seperated by ,) :").split(",")))

print()

time,result=Scanner.port_scan(ip,rg[0],rg[1])
print()
print("-"*130)
print(f"Total time taken by scanner: {time:.2f}s")
print("-"*130)
print()
print(f"{'PORT':<11} | {'STATUS':<22} | {'SERVICE':<15} | {'TIME':<14}")
print()
print("-"*130)
for port,st,ser,t in result:
    if st=="Open":
        co=color.green
    else:
        co=color.red
    print(f"Port no: {port} | {co}{st:<22}{color.reset} | {ser:<15} | {f"{t:.6f}s":<15}")

print("-"*130)
s=input("Do you want to save the report? (yes/no) ").lower()
if s=="yes" :
    report.scan_report(result)
    print("\nREPORT SAVED SUCCESSFULLY")



