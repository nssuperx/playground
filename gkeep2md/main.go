package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"html/template"
	"io"
	"os"
	"path/filepath"
	"strings"
)

type GKeepLabel struct {
	Name string
}

type GKeepJson struct {
	Title       string
	TextContent string
	Labels      []GKeepLabel
}

func readFile(filePath string) []byte {
	file, err := os.Open(filePath)
	if err != nil {
		panic(err)
	}
	bytes, err := io.ReadAll(file)
	if err != nil {
		panic(err)
	}
	return bytes
}

func main() {
	filePath := flag.String("f", ".", "filePath")
	flag.Parse()

	jsonBytes := readFile(*filePath)

	var gKeep GKeepJson

	if err := json.Unmarshal(jsonBytes, &gKeep); err != nil {
		panic(err)
	}

	var gKeepLabels []string
	for _, v := range gKeep.Labels {
		gKeepLabels = append(gKeepLabels, v.Name)
	}

	fileName := filepath.Base(*filePath)
	saveDir := filepath.Dir(*filePath)
	saveFilename := fileName[:len(fileName)-len(filepath.Ext(fileName))] + ".md"
	fmt.Println(saveFilename)

	dirName := filepath.Join(saveDir, strings.Join(gKeepLabels, "_"))
	if err := os.MkdirAll(dirName, 0755); err != nil {
		panic(err)
	}

	saveFile, err := os.Create(filepath.Join(dirName, saveFilename))
	if err != nil {
		panic(err)
	}
	defer saveFile.Close()
	
	tmpl, err := template.New("md").Parse("# {{.Title}}\n\n{{.TextContent}}\n")
	if err != nil {
		panic(err)
	}
	writer := io.Writer(saveFile)
	if err = tmpl.Execute(writer, gKeep); err != nil {
		panic(err)
	}
}
