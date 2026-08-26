import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"
import type { Shipment } from "./client";

function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

function getLatestStatus(shipment: Shipment) {
  return shipment.timeline[shipment.timeline.length - 1].status
}

function getShipmentsCountWithStatus(
  shipments: Shipment[],
  status: string
) {
  console.log(shipments)
  return shipments.filter((shipment) => getLatestStatus(shipment) === status).length;
}

export { cn, getLatestStatus, getShipmentsCountWithStatus as getShipmentsCountForStatus }