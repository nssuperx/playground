package main

import (
	"fmt"
	"os"
	"text/template"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: main.exe <スクリプト名>")
		os.Exit(1)
	}
	scriptName := os.Args[1]

	hlslBytes, err := os.ReadFile(scriptName + "/shader.hlsl")
	if err != nil {
		panic(err)
	}

	tmpl, err := template.ParseFiles(scriptName + "/tmpl.lua")
	if err != nil {
		panic(err)
	}

	anm2, err := os.Create(scriptName + "/" + scriptName + ".anm2")
	if err != nil {
		panic(err)
	}
	defer anm2.Close()

	err = tmpl.Execute(anm2, map[string]string{
		"psmain": scriptName,
		"hlsl":   string(hlslBytes),
	})
	if err != nil {
		panic(err)
	}
}
