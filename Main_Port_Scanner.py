import Scanner
import color
import report

val=input("Host or IP? ").lower()
if val=="host":
    ip=Scanner.host_name(input("Enter Host name: "))
elif val=="ip":
    ip=input("Enter IP address: ")

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

report.scan_report(result)



