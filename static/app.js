const form = document.getElementById("shorten-form");
const input = document.getElementById("url-input");
const button = document.getElementById("shorten-button");
const result = document.getElementById("result");
const message = document.getElementById("message");
const historyBox = document.getElementById("history");

function showMessage(text, isError = false) {
  message.textContent = text;
  message.style.color = isError ? "#c03950" : "#77738b";
}

function safeLink(url) {
  const link = document.createElement("a");
  link.href = url;
  link.target = "_blank";
  link.rel = "noopener noreferrer";
  link.textContent = url;
  return link;
}

async function copyText(text, buttonElement) {
  try {
    await navigator.clipboard.writeText(text);
    buttonElement.textContent = "Copied!";
  } catch {
    window.prompt("Copy your short URL:", text);
  }
}

function createLinkCard(link) {
  const card = document.createElement("article");
  card.className = "link-item";

  const top = document.createElement("div");
  top.className = "link-item-top";

  const shortCode = document.createElement("div");
  shortCode.className = "short-code";
  shortCode.textContent = link.short_url;

  const clicks = document.createElement("span");
  clicks.className = "click-badge";
  clicks.textContent = `${link.clicks} clicks`;

  top.append(shortCode, clicks);

  const target = document.createElement("div");
  target.className = "target-url";
  target.textContent = link.target_url;

  const bottom = document.createElement("div");
  bottom.className = "link-item-bottom";

  const date = document.createElement("span");
  date.className = "created-at";
  date.textContent = `Created: ${link.created_at}`;

  const copy = document.createElement("button");
  copy.className = "copy-button";
  copy.type = "button";
  copy.textContent = "Copy link";
  copy.addEventListener("click", () => copyText(link.short_url, copy));

  bottom.append(date, copy);
  card.append(top, target, bottom);
  return card;
}

async function loadHistory() {
  historyBox.replaceChildren();
  const loading = document.createElement("div");
  loading.className = "empty-state";
  loading.textContent = "Loading your links…";
  historyBox.append(loading);

  try {
    const response = await fetch("/api/links");
    if (!response.ok) throw new Error("Could not load link history");

    const links = await response.json();
    document.getElementById("total-links").textContent = links.length;
    document.getElementById("total-clicks").textContent =
      links.reduce((sum, link) => sum + Number(link.clicks || 0), 0);

    historyBox.replaceChildren();

    if (links.length === 0) {
      const empty = document.createElement("div");
      empty.className = "empty-state";
      empty.textContent = "No links yet. Create your first short link above!";
      historyBox.append(empty);
      return;
    }

    for (const link of links) {
      historyBox.append(createLinkCard(link));
    }
  } catch (error) {
    historyBox.replaceChildren();
    const failed = document.createElement("div");
    failed.className = "empty-state";
    failed.textContent = `${error.message}. Check that LinkForge is running.`;
    historyBox.append(failed);
  }
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const url = input.value.trim();

  result.classList.add("hidden");
  showMessage("");
  button.disabled = true;
  button.textContent = "Creating…";

  try {
    const response = await fetch("/api/shorten", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url })
    });

    const data = await response.json();

    if (!response.ok) {
      const detail = Array.isArray(data.detail)
        ? data.detail.map(item => item.msg).join(", ")
        : data.detail;
      throw new Error(detail || "Could not shorten this URL");
    }

    result.replaceChildren();

    const title = document.createElement("div");
    title.className = "result-title";
    title.textContent = "YOUR SHORT LINK IS READY";

    const link = document.createElement("div");
    link.className = "result-link";
    link.append(safeLink(data.short_url));

    const copy = document.createElement("button");
    copy.className = "copy-button";
    copy.type = "button";
    copy.textContent = "Copy short link";
    copy.addEventListener("click", () => copyText(data.short_url, copy));

    result.append(title, link, copy);
    result.classList.remove("hidden");
    input.value = "";
    showMessage("Link created successfully!");
    await loadHistory();
  } catch (error) {
    showMessage(error.message, true);
  } finally {
    button.disabled = false;
    button.innerHTML = 'Create short link <span>→</span>';
  }
});

document.getElementById("refresh-button").addEventListener("click", loadHistory);
loadHistory();
