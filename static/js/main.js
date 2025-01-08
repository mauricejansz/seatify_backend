document.addEventListener("DOMContentLoaded", function () {
    const deletedCategories = new Set();
    const deletedMenuItems = new Set();
    const deletedTables = new Set();
    const deletedSlots = new Set();

    // Add Line
    document.querySelectorAll(".add-line-btn").forEach((btn) => {
        btn.addEventListener("click", function () {
            const table = this.previousElementSibling.querySelector("tbody");
            const emptyLine = table.querySelector(".empty-line");
            if (emptyLine) {
                const newRow = emptyLine.cloneNode(true);
                newRow.style.display = "";
                newRow.classList.remove("empty-line");
                newRow.querySelectorAll("input").forEach((input) => {
                    input.value = ""; // Clear any existing values
                });
                table.appendChild(newRow);
            } else {
                console.error("No .empty-line found in table. Ensure your HTML structure includes a hidden .empty-line row.");
            }
        });
    });

    // Remove Line
    document.addEventListener("click", function (e) {
        if (e.target.classList.contains("remove-line-btn")) {
            const row = e.target.closest("tr");
            if (row.classList.contains("menu-item")) {
                const menuItemId = row.getAttribute("data-menu-item-id");
            if (menuItemId) {
                deletedMenuItems.add(menuItemId); // Add to deleted items
            }
            } else if (row.classList.contains("table-item")) {
                const tableId = row.getAttribute("data-table-id");
                if (tableId) {
                    deletedTables.add(tableId); // Add to deleted items
                }
            } else if (row.classList.contains("slot-item")) {
                const slotId = row.getAttribute("data-slot-id");
                if (slotId) {
                    deletedSlots.add(slotId); // Add to deleted items
                }
            }
            row.remove(); // Remove the row from the DOM
        }
    });

    // Add Category
    document.getElementById("add-category-btn").addEventListener("click", function () {
        const container = document.getElementById("menu-container");
        const categoryHtml = `
            <div class="menu-category" data-category-id="new">
                <div class="d-flex justify-content-between align-items-center">
                    <h5 class="mt-3">
                        <input type="text" class="form-control editable-input category-name" placeholder="New Category">
                    </h5>
                    <button class="btn btn-danger remove-category-btn">Remove Category</button>
                </div>
                <table class="table table-dark table-striped menu-items-table">
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>Description</th>
                            <th>Price</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="empty-line" style="display: none;">
                            <td><input type="text" class="form-control editable-input" id="menu-item-name" placeholder="Item Name"></td>
                            <td><input type="text" class="form-control editable-input" id="menu-item-description" placeholder="Description"></td>
                            <td><input type="number" class="form-control editable-input" id="menu-item-price" placeholder="Price"></td>
                            <td><button class="btn btn-danger remove-line-btn">Remove</button></td>
                        </tr>
                    </tbody>
                </table>
                <button class="btn btn-primary add-line-btn">Add Line</button>
            </div>
        `;
        container.insertAdjacentHTML("beforeend", categoryHtml);
    });

    // Mark category for deletion
    document.addEventListener("click", function (e) {
        if (e.target.classList.contains("remove-category-btn")) {
            const categoryDiv = e.target.closest(".menu-category");
            const categoryId = categoryDiv.getAttribute("data-category-id");

            if (confirm("Are you sure you want to remove this category?")) {
                if (categoryId) {
                    deletedCategories.add(categoryId);
                }
                categoryDiv.remove();
            }
        }
    });

    // Save Button
    document.getElementById("save-btn").addEventListener("click", function () {
        const data = {
            "restaurant-name": document.getElementById("restaurant-name").value,
            phone: document.getElementById("phone").value,
            address: document.getElementById("address").value,
            description: document.getElementById("description").value,
            latitude: document.getElementById("latitude").value,
            longitude: document.getElementById("longitude").value,
            cuisine: document.getElementById("cuisine").value,
            deleted_categories: Array.from(deletedCategories),
            deleted_menu_items: Array.from(deletedMenuItems),
            new_categories: [],
            updated_categories: [],
            new_menu_items: [],
            updated_menu_items: [],
            deleted_tables: Array.from(deletedTables),
            new_tables: [],
            updated_tables: [],
            deleted_slots: Array.from(deletedSlots),
            new_slots: [],
            updated_slots: [],
        };
        const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

        const restaurantId = document.getElementById("save-btn").getAttribute("data-restaurant-id");

        // Collect category data
        document.querySelectorAll(".menu-category").forEach((category) => {
            const categoryId = category.getAttribute("data-category-id");
            const categoryName = category.querySelector(".category-name").value;

            if (categoryId === "new") {
                data.new_categories.push({name: categoryName});
            } else {
                data.updated_categories.push({id: categoryId, name: categoryName});
            }

            // Collect menu items for this category
            category.querySelectorAll(".menu-items-table tbody tr:not(.empty-line)").forEach((row) => {
                const itemNameInput = row.querySelector("#menu-item-name");
                const itemDescriptionInput = row.querySelector("#menu-item-description");
                const itemPriceInput = row.querySelector("#menu-item-price");

                if (itemNameInput && itemDescriptionInput && itemPriceInput) {
                    const itemName = itemNameInput.value;
                    const itemDescription = itemDescriptionInput.value;
                    const itemPrice = itemPriceInput.value;

                    const menuItemId = row.getAttribute("data-menu-item-id"); // Fetch the menu item ID

                    if (categoryId === "new" || !menuItemId) {
                        data.new_menu_items.push({
                            category_name: categoryName,
                            name: itemName,
                            description: itemDescription,
                            price: itemPrice,
                        });
                    } else {
                        if (menuItemId) {
                            data.updated_menu_items.push({
                                id: menuItemId, // Include the ID for updated items
                                category_id: categoryId,
                                name: itemName,
                                description: itemDescription,
                                price: itemPrice,
                            });
                        }
                    }
                }
            });
        });

        document.querySelectorAll("#table-info tbody tr:not(.empty-line)").forEach((row) => {
            const tableId = row.getAttribute("data-table-id");
            const tableNumber = row.querySelector("td:nth-child(1) input").value;
            const tableCapacity = row.querySelector("td:nth-child(2) input").value;

            if (!tableNumber || !tableCapacity) return; // Skip invalid entries

            if (tableId) {
                // Updated table
                data.updated_tables.push({
                    id: tableId,
                    number: tableNumber,
                    capacity: tableCapacity,
                });
            } else {
                // New table
                data.new_tables.push({
                    number: tableNumber,
                    capacity: tableCapacity,
                });
            }
        });

        document.querySelectorAll("#available-slots tbody tr:not(.empty-line)").forEach((row) => {
            const slotId = row.getAttribute("data-slot-id");
            const slotTime = row.querySelector("#slot-item-time").value;
            const slotDate = row.querySelector("#slot-item-date").value;
            const slotTable = row.querySelector("#slot-table-number").value;

            if (!slotTime || !slotTable || !slotDate) return; // Skip invalid entries

            if (slotId) {
                // Updated slot
                data.updated_slots.push({
                    id: slotId,
                    time: slotTime,
                    table_id: slotTable,
                    date: slotDate,
                });
            } else {
                // New slot
                data.new_slots.push({
                    time: slotTime,
                    table_id: slotTable,
                    date: slotDate,
                });
            }
        });

        console.log("Data to save:", data);

        fetch(`/restaurant/${restaurantId}/save/`, {
            method: "POST",
            headers: {"Content-Type": "application/json", "X-CSRFToken": csrfToken},
            body: JSON.stringify(data),
        })
            .then((response) => {
                if (response.ok) {
                    alert("Changes saved!");
                    deletedCategories.clear();
                    deletedMenuItems.clear();
                    deletedTables.clear();
                } else {
                    alert("Failed to save.");
                }
            })
            .catch((error) => {
                console.error("Error:", error);
            });
    });
});