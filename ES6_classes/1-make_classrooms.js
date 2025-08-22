import ClassRoom from "./0-classroom";


export default function initializeRooms() {
  const rooms = [];
  const sizes = [19, 20, 34];
  for (const size of sizes) {
    rooms.push(new ClassRoom(size));
  }
  return rooms;
}
