#!/usr/bin/env python3
"""
Test script for the Flask application
Run this after starting the containers with 'docker compose up -d'
"""

import requests
import time
import sys

def test_application():
    base_url = "http://localhost:8080"
    
    print("Testing Flask Application with PostgreSQL")
    print("=" * 50)
    
    # Wait a moment for containers to be ready
    print("Waiting for containers to be ready...")
    time.sleep(5)
    
    try:
        # Test 1: Verify connection to database
        print("\n1. Testing database connection...")
        response = requests.get(f"{base_url}/")
        if response.status_code == 200:
            print(f"✓ Database connection successful: {response.text}")
        else:
            print(f"✗ Database connection failed: {response.status_code}")
            return False
            
        # Test 2: Add a message
        print("\n2. Adding a test message...")
        response = requests.post(f"{base_url}/add?texto=HolaDocker")
        if response.status_code == 200:
            print(f"✓ Message added successfully: {response.text}")
        else:
            print(f"✗ Failed to add message: {response.status_code}")
            return False
            
        # Test 3: Add another message
        print("\n3. Adding another test message...")
        response = requests.post(f"{base_url}/add?texto=TestMessage2")
        if response.status_code == 200:
            print(f"✓ Second message added: {response.text}")
        else:
            print(f"✗ Failed to add second message: {response.status_code}")
            return False
            
        # Test 4: List all messages
        print("\n4. Retrieving all messages...")
        response = requests.get(f"{base_url}/list")
        if response.status_code == 200:
            messages = response.json()
            print(f"✓ Retrieved messages: {messages}")
            if len(messages['mensajes']) >= 2:
                print("✓ Data persistence working correctly!")
            else:
                print("✗ Expected at least 2 messages")
                return False
        else:
            print(f"✗ Failed to retrieve messages: {response.status_code}")
            return False
            
        print("\n" + "=" * 50)
        print("✓ All tests passed! Application is working correctly.")
        return True
        
    except requests.exceptions.ConnectionError:
        print("✗ Cannot connect to the application. Make sure containers are running.")
        print("Run: docker compose up -d")
        return False
    except Exception as e:
        print(f"✗ Error during testing: {e}")
        return False

if __name__ == "__main__":
    success = test_application()
    sys.exit(0 if success else 1)
