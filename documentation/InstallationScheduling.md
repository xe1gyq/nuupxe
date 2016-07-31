# Scheduling

```sh
repeater@stn8148:~/custom$ nano custom_decode 
...

# NuupXe Project, Module Mode, Production
if [ "$1" = "P1" ] ; then cd "$CUSTOM"/nuupxe; python nuupxe.py -m weather ; exit 1 ; fi

# NuupXe  Project, Module Mode, Experimental
if [[ "$1" == PS* ]] ; then cd "$CUSTOM"/nuupxe; python nuupxe.py -d $1 ; exit 1 ; fi

exit 0 
repeater@stn8148:~/custom$ 
```

```sh
repeater@stn8148:~/custom$ nano custom.crons
#Reporte meteorologico cada 3 horas
30 0,3,6,9,12,15,18,21 * * * (/home/irlp/scripts/decode P4 &>/dev/null 2>&1)
repeater@stn8148:~/custom$ 
```
