import { Metadata } from "next";
import { OverviewMap } from "./components/OverviewMap";

export const metadata: Metadata = {
  title: "Energy Sim | Overview",
  description: "Overview to energy simulator",
};

export default function OverviewPage() {
  return <OverviewMap />
}
