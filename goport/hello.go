package main

import (
	"log"

	"github.com/bisoncorps/mplayer"
)

func main() {
	p, err := mplayer.GetPlayer("mpv")
	if err != nil {
		log.Fatal(err)
	}
	// urls can be remote too
	p.SetURL("/Users/hasrinismail/Downloads/freeetv/pyport/hachi.mp4")
	p.SetTitle("Jumanji MP4")
	p.Play()
}
