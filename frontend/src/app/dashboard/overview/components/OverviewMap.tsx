"use client";

import React from "react";
import { Map } from "react-map-gl";
import maplibregl from "maplibre-gl";
import DeckGL from "@deck.gl/react";
import { ScatterplotLayer } from "@deck.gl/layers";
import { RGBAColor } from "@deck.gl/core";

const MALE_COLOR: RGBAColor = [0, 128, 255];
const FEMALE_COLOR: RGBAColor = [255, 0, 128];

const DATA_URL =
  "https://raw.githubusercontent.com/visgl/deck.gl-data/master/examples/scatterplot/manhattan.json";

const INITIAL_VIEW_STATE = {
  longitude: -74,
  latitude: 40.7,
  zoom: 11,
  maxZoom: 16,
  pitch: 0,
  bearing: 0,
};

export function OverviewMap({
  data = DATA_URL,
  radius = 30,
  maleColor = MALE_COLOR,
  femaleColor = FEMALE_COLOR,
  mapStyle = "https://basemaps.cartocdn.com/gl/positron-nolabels-gl-style/style.json",
}) {
  const layers = [
    new ScatterplotLayer({
      id: "scatter-plot",
      data,
      radiusScale: radius,
      radiusMinPixels: 0.25,
      getPosition: (d: any) => [d[0], d[1], 0],
      getFillColor: (d: any) => (d[2] === 1 ? maleColor : femaleColor),
      getRadius: 1,
      updateTriggers: {
        getFillColor: [maleColor, femaleColor],
      },
    }),
  ];

  return (
    <div className="flex h-full">
      <div className="bg-grey-400 relative flex-grow overflow-clip flex">
        <DeckGL
          layers={layers}
          initialViewState={INITIAL_VIEW_STATE}
          controller={true}
        >
          <Map
            reuseMaps
            //@ts-ignore
            mapLib={maplibregl}
            mapStyle={mapStyle}
            preventStyleDiffing={true}
          />
        </DeckGL>
      </div>
    </div>
  );
}
