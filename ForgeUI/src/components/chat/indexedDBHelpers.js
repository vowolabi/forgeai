import { openDB } from 'idb';

// Initialize IndexedDB
async function initDB() {
    return openDB('chat-db', 1, {
        upgrade(db) {
            db.createObjectStore('messages', { keyPath: 'id', autoIncrement: true });
        },
    });
}

// Save messages to IndexedDB
async function saveMessageHistory(history) {
    const db = await initDB();
    const tx = db.transaction('messages', 'readwrite');
    await tx.store.clear();
    for (const message of history) {
        await tx.store.add(message);
    }
    await tx.done;
}

// Add or update a single message in IndexedDB
async function addOrUpdateMessage(message) {
    const db = await initDB();
    const tx = db.transaction('messages', 'readwrite');
    await tx.store.put(message);
    await tx.done;
}

// Load messages from IndexedDB
async function loadMessageHistory() {
    const db = await initDB();
    return db.getAll('messages');
}

export { saveMessageHistory, addOrUpdateMessage, loadMessageHistory };
